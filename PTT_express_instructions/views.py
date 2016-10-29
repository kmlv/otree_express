from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


# class MyPage(Page):
#
#     def vars_for_template(self):
#         return {
#             'treatment': self.participant.treatment
#         }


class Instructions(Page):
    pass

class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Instructions,
    Results
]
