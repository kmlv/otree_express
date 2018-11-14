# -*- coding: utf-8 -*-
# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree import widgets
from otree.common import Currency as c, currency_range
import random
# </standard imports>




class Constants(BaseConstants):
    name_in_url = 'demograp'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_Demographics = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_CognitiveReflectionTest = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    def set_payoff(self):
        """Calculate payoff, which is zero for the survey"""
        self.payoff = 0

    q_country = models.CharField()

    q_age = models.PositiveIntegerField(verbose_name='What is your age?',
                                        choices=range(13, 125),
                                        initial=None)

    q_station = models.PositiveIntegerField(verbose_name='What is your computer station number? (see white sticker on computer or ask experimenter)',
                                        choices=range(1, 17),
                                        initial=None)

    q_gender = models.CharField(initial=None,
                                choices=['Male', 'Female', 'Other'],
                                verbose_name='What is your gender?',
                                widget=widgets.RadioSelect())
    q_income = models.PositiveIntegerField(verbose_name='What is the approximate annual income of your family?',
                                           choices=[
                                               [1, 'less than $15,000'],
                                               [2, '$15,000 - $29,999'],
                                               [3, '$30,000 - $59,999'],
                                               [4, '$60,000 - $99,999'],
                                               [5, '$100,000 - $199,999'],
                                               [6, '$200,000 or more'],
                                               [7, 'I rather not answer this question'],
                                           ]
                                           )

    q_zipcode = models.PositiveIntegerField(verbose_name='What is the zip code where you grew up?')

    q_opinion = models.CharField(initial=None,
                                 verbose_name='Were the instructions provided in this experiment clear and useful?',
                                 choices=['Yes', 'No'],
                                 widget=widgets.RadioSelect())

    crt_bat = models.PositiveIntegerField()

    crt_widget = models.PositiveIntegerField()

    crt_lake = models.PositiveIntegerField()
