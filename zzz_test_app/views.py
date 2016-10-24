from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class MyPage1(Page):
    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class g1Waits(WaitPage):
    wait_for_all_groups = True

    # def is_displayed(self):
    #     self.group.g

class Results(Page):
    pass


page_sequence = [
    MyPage,
    g1Waits,
    MyPage1,
    ResultsWaitPage,
    Results
]
