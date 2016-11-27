from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Kristian Lopez Vargas'

doc = """
This is a simple page that is meant to be the cover page of any experiment in the LEEPS Lab
"""


class Constants(BaseConstants):
    name_in_url = '_Cover_Welcome'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    time_InitialCover = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
