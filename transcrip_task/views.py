# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range, safe_json
from .models import Constants, levenshtein, distance_and_ok
from django.conf import settings



class Instructions(Page):
    form_model = models.Player
    form_fields = ['time_Instructions']


class Transcription(Page):
    form_model = models.Player
    form_fields = ['transcribed_text', 'time_Transcription']

    def vars_for_template(self):
        return {
            'image_path': 'transcrip_task/paragraphs/{}.png'.format(
                self.round_number),
            'reference_text': Constants.reference_texts[self.round_number - 1],
            'debug': settings.DEBUG,
            'required_accuracy':  100 * (1 - Constants.allowed_error_rates[self.round_number - 1])

        }

    def transcribed_text_error_message(self, transcribed_text):
        reference_text = Constants.reference_texts[self.round_number - 1]
        allowed_error_rate = Constants.allowed_error_rates[
            self.round_number - 1]
        distance, ok = distance_and_ok(transcribed_text, reference_text,
                                       allowed_error_rate)
        if ok:
            self.player.levenshtein_distance = distance
        else:
            if allowed_error_rate == 0:
                return "The transcription should be exactly the same as on the image."
            else:
                return "This transcription appears to contain too many errors."

    def before_next_page(self):
        self.player.payoff = 0

class Summary(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        data_series = []
        for prev_player in self.player.in_all_rounds():
            data = {
                'round_number': prev_player.round_number,
                'reference_text_length': len(Constants.reference_texts[prev_player.round_number - 1]),
                'transcribed_text_length': len(prev_player.transcribed_text),
                'distance': prev_player.levenshtein_distance,
            }
            data_series.append(data)

        return {'data_series': data_series}


class ResultsTranscrip(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        data_series = []
        for prev_player in self.player.in_all_rounds():
            data = {
                'round_number': prev_player.round_number,
                'reference_text_length': len(Constants.reference_texts[prev_player.round_number - 1]),
                'transcribed_text_length': len(prev_player.transcribed_text),
                'distance': prev_player.levenshtein_distance,
            }
            data_series.append(data)

        return {'data_series': data_series}


class Send(Page):
    form_model = models.Group
    form_fields = ['sent_amount', 'time_Send']

    def is_displayed(self):
        return self.player.id_in_group == 1


class SendBack(Page):
    form_model = models.Group
    form_fields = ['sent_back_amount', 'time_SendBack']

    def is_displayed(self):
        return self.player.id_in_group == 2

    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }

    def sent_back_amount_choices(self):
        return currency_range(
            c(0),
            self.group.sent_amount * Constants.multiplication_factor,
            c(1)
        )


class Results(Page):
    def vars_for_template(self):
        return {
            'tripled_amount': self.group.sent_amount * Constants.multiplication_factor
        }


class WaitForP1(WaitPage):
    pass


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_payoffs()


page_sequence = [Instructions,
                 Transcription,
                 ResultsTranscrip,
                 Send,
                 WaitForP1,
                 SendBack,
                 ResultsWaitPage,
                 Results,
                 ]
