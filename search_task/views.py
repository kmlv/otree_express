from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    pass


class SearchTask(Page):
    form_model = models.Player
    form_fields = ['task_reward']

    def vars_for_template(self):
        return {
            'target_income': self.player.target_income
        }
    def before_next_page(self):
        self.participant.vars['task_income'] = self.player.task_reward
        # self.player.intermediate_reward = self.player.task_reward + self.group.treatment_endowment



class PracticeTask(Page):
    pass

page_sequence = [
    PracticeTask,
    SearchTask
]
