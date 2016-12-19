from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class PracticeTask(Page):
    form_model = models.Player
    form_fields = ['time_PracticeTask']
    #pass
    # timeout_seconds = 200


class SearchTask(Page):
    # timeout_seconds = 400

    form_model = models.Player
    form_fields = ['task_reward', 'time_SearchTask']

    def vars_for_template(self):
        return {
            'target_income': self.player.target_income,
            'maxScreens': self.player.maxScreens,
            'role': self.player.role(),
            'screenTime': self.player.screenTime,
        }

    def before_next_page(self):
        self.participant.vars['task_income'] = self.player.task_reward
#        self.participant.vars['task_income_other'] = self.get_others_in_group()[0].task_reward
        if self.player.role() == 'A':
            self.participant.vars['task_income_other'] = self.group.get_player_by_role('B').task_reward
        elif self.player.role() == 'B':
            self.participant.vars['task_income_other'] = self.group.get_player_by_role('A').task_reward
#        return True
        # self.player.intermediate_reward = self.player.task_reward + self.group.treatment_endowment


class GameInstructions(Page):
    form_model = models.Player
    form_fields = ['time_GameInstructions']
    #pass

    # timeout_seconds = 400

page_sequence = [
    GameInstructions,
    PracticeTask,
    SearchTask
]
