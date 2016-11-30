# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree import forms
from otree.common import Currency as c, currency_range
import random
from django.core.validators import MaxLengthValidator

# </standard imports>

author = 'Paola  Villa'

doc = """
This is a task that requires real effort from participants. Subjects are shown two images of incomprehensible text.
Subjects are required to transcribe (copy) the text into a text entry field. The quality of a subject's transcription
 is measured by the <a href="http://en.wikipedia.org/wiki/Levenshtein_distance">Levenshtein distance</a>.
"""
def levenshtein(a, b):
    """Calculates the Levenshtein distance between a and b."""
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n

    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)

    return current[n]


def distance_and_ok(transcribed_text, reference_text, max_error_rate):
    error_threshold = len(reference_text) * max_error_rate
    distance = levenshtein(transcribed_text, reference_text)
    ok = distance <= error_threshold
    return distance, ok


class Constants(BaseConstants):
    name_in_url = 'transcrip_task'
    players_per_group = 2
    num_rounds = 1

    endowment = c(10)
    multiplication_factor = 3

    allowed_error_rates = [0, 0.03]
    #show_transcription_1 = True

    reference_texts = [
        "Munakusqay urpi, uyaririllaway, sunquyta paqumaq munakapullaway."
    ]
    paragraph_count = len(reference_texts)



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    time_Send = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_SendBack = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    sent_amount = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
        doc="""Amount sent by P1""",
    )

    sent_back_amount = models.CurrencyField(
        doc="""Amount sent back by P2""",
    )

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):
    time_Instructions = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_Transcription = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    transcribed_text = models.TextField()
    distance_1 = models.PositiveIntegerField()
    levenshtein_distance = models.PositiveIntegerField()

    def set_payoff(self):
        self.payoff = 0
