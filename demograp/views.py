# -*- coding: utf-8 -*-
from __future__ import division
from . import models
from ._builtin import Page, WaitPage
from otree.common import Currency as c, currency_range
from .models import Constants


class Demographics(Page):
    form_model = models.Player
    form_fields = ['q_country',
                   'q_age',
                   'q_gender',
                   'q_income',
                   'q_zipcode',
                   'q_opinion',
                   'time_Demographics',
                   'q_station'
                   ]


class CognitiveReflectionTest(Page):
    form_model = models.Player
    form_fields = ['crt_bat',
                   'crt_widget',
                   'crt_lake',
                   'time_CognitiveReflectionTest',
                   ]

    def before_next_page(self):
        self.player.set_payoff()


page_sequence = [
    Demographics,
    # CognitiveReflectionTest
]
