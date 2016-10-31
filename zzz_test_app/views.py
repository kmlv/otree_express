from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage1(Page):
    form_model = models.Player
    form_fields = ['contribution']

    #def is_displayed(self):
     #   return self.player.id_in_group != 3

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class g1Waits(WaitPage):
    wait_for_all_groups = True

    # def is_displayed(self):
    #     self.group.g

class Results(Page):
    pass


page_sequence = [
    MyPage1,
    g1Waits,
    ResultsWaitPage,
    Results
]
