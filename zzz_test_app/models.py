from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'zzz_test_app'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def before_session_starts(self):
        self.set_group_matrix([[1], [2]])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass

    # roles
    # def role(self):
    #     i = 0
    #     for grupo in self.group
    #     return self.