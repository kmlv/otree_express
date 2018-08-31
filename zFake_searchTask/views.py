from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):

    def before_next_page(self):

        # passes task reward to task_income
        self.participant.vars['task_income'] = self.player.task_income
    #timeout_seconds = 2
    timeout_seconds = .1


class temp_WillingnessBList(Page):
    form_model = models.Group
    form_fields = ['b_willing']


page_sequence = [
    MyPage
]
