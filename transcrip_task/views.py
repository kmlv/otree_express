# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range, safe_json
from .models import Constants, levenshtein, distance_and_ok
from django.conf import settings



class Instructions(Page):
    form_model = 'player'
    form_fields = ['time_Instructions']


class Transcription(Page):
    form_model = 'player'
    form_fields = ['transcribed_text']

    def vars_for_template(self):
        return {
            'image_path': 'transcrip_task/paragraphs/{}.png'.format(
                self.round_number),
            'reference_text': Constants.reference_texts[self.round_number - 1],
            'debug': settings.DEBUG,
            'required_accuracy':  100 * (1 - self.session.config['allowed_error_rates'][self.round_number - 1])

        }

    def transcribed_text_error_message(self, transcribed_text):
        reference_text = Constants.reference_texts[self.round_number - 1]
        allowed_error_rate = self.session.config['allowed_error_rates'][
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

class ResultsTranscrip(Page):
    form_model = models.Player

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


    def before_next_page(self):
        self.participant.vars['distance'] = self.player.levenshtein_distance
        # ask if this save info from all rounds or just the last one
        # Ask how to save data_series as participant vars

page_sequence = [Instructions,
                 Transcription,
                 ResultsTranscrip,
                 ]
