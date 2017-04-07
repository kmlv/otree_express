from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'zFake_searchTask'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    def before_session_starts(self):
        self.debug_mode = self.session.config['debug']

        # passing list of target income into task income
        for player in self.get_players():
            if 'targetIncome' in self.session.config:
                if len(self.session.config['targetIncome']) == len(self.get_players()):
                    player.task_income = self.session.config['targetIncome'][player.id_in_group -1]
                elif len(self.session.config['targetIncome']) == 1:
                    player.task_income = self.session.config['targetIncome'][0]
                else:
                    assert False, "targetIncome length is not correct in config file"
            else:
                player.task_income = 10


class Group(BaseGroup):
    b_willing = models.DecimalField(min=0, max_digits=6, decimal_places=3)


class Player(BasePlayer):
    task_income = models.CurrencyField()



