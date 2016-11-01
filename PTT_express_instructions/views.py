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

    def vars_for_template(self):
        return {
            'treatment': self.group.treatment,
            'role': self.player.role(),
            'value_type': self.group.value_type,
            'elicitation_method': self.group.elicitation_method,
            'BDM_type': self.group.BDM_type,
            'participation_fee': self.session.config['participation_fee'],
            'endowment': self.player.endowment,
            'BDM_uplimit': self.group.BDM_uplimit
        }


class ControlQuestions(Page):
    pass


class Results(Page):
    pass

# class ResultsWaitPage(WaitPage):
#
#     def after_all_players_arrive(self):
#         pass
#
#


page_sequence = [
    Instructions
    # ,
    # ControlQuestions,
    # Results
]
