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

    form_model = models.Player

    def get_form_fields(self):
        if self.group.treatment in ['NM', 'FM']:
            return [
                'ctrlQ_anonymity',
                'ctrlQ_who_transfers',
                'ctrlQ_A_earnings',
                'ctrlQ_B_earnings'
            ]
        elif self.group.treatment in ['DM', 'TP']:
            return [
                'ctrlQ_anonymity',
                'ctrlQ_who_transfers',
                'ctrlQ_B_always_sends',
                'ctrlQ_A_earnings',
                'ctrlQ_B_sends_message',
                'ctrlQ_B_earnings',
            ]

    def ctrlQ_anonymity_error_message(self, value):
        if not (value == 'Not'):
            return 'The correct answer is  `Not` -- Once you are paired with another participant, ' \
                   'will you NEVER know the identity of the other participant'

    def ctrlQ_B_earnings_error_message(self, value):
        if self.group.treatment in ['NM', 'FM']:
            if not (value == '13.00 - X'):
                return 'The correct answer is `13.00 - X` since B receives an endowment of 3.00, a task income of ' \
                       '10.00 and Role A took X from his/her account.'
        if self.group.treatment in ['DM', 'TP']:
            if self.group.value_type == 'WTP' and not (value == '13.00 - X - Z'):
                return 'The correct answer is `13.00 - X - Z` since B receives an endowment of 3.00, a task income of ' \
                       '10.00 and Role A took X from his/her account.'
            if self.group.value_type == 'WTA' and not (value == '13.00 - X + Z'):
                return 'The correct answer is `13.00 - X + Z` since B receives an endowment of 3.00, a task income of ' \
                       '10.00 and Role A took X from his/her account.'



    def vars_for_template(self):
        return {
            'recipient': (self.group.treatment == 'DM')*'the participant with Role A' +
                         (self.group.treatment == 'TP')*'the Reader'
        }

############################################################################################

page_sequence = [
    Instructions,
    ControlQuestions
]










# form_fields = [
#             'ctrlQ_anonymity',
#             'ctrlQ_who_transfers',
#             'ctrlQ_B_always_sends',
#             'ctrlQ_A_earnings',
#             'ctrlQ_B_sends_message',
#             'ctrlQ_B_earnings'
#         ]
