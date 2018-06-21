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
    #form_model = models.Player
    #form_fields = ['time_Instructions']
    def vars_for_template(self):
        return {
            'treatment': self.group.treatment,
            'role': self.player.role(),
            'value_type': self.group.value_type,
            'elicitation_method': self.group.elicitation_method,
            'BDM_type': self.group.BDM_type,
            'participation_fee': self.session.config['participation_fee'],
            'endowment': self.player.endowment,
            'BDM_uplimit': self.group.BDM_uplimit,
            'points': self.session.config['USE_POINTS'],
        }


    # timeout_seconds = 400


class ControlQuestions(Page):
    form_model = models.Player

    # timeout_seconds = 400

    def get_form_fields(self):
        if self.group.treatment in ['NM', 'FM']:
            return [
                'ctrlQ_anonymity',
                'ctrlQ_who_transfers',
                'ctrlQ_A_earnings',
                'ctrlQ_B_earnings',
                #'time_ControlQuestions'
            ]
        elif self.group.treatment in ['DM', 'TP']:
            return [
                'ctrlQ_anonymity',
                'ctrlQ_who_transfers',
                'ctrlQ_B_always_sends',
                'ctrlQ_A_earnings',
                'ctrlQ_B_sends_message',
                'ctrlQ_B_earnings',
                #'time_ControlQuestions'
            ]
        elif self.group.treatment in ['TP-R']:
            return [
                'ctrlQ_anonymity',
                'ctrlQ_who_transfers',
                #'time_ControlQuestions'
            ]
        

    def iterate_fc(self):
        self.player.fields_checked = self.player.fields_checked + 1
    
    def on_first(self):
        return self.player.fields_checked < self.player.number_of_questions

    def ctrlQ_anonymity_error_message(self, value):
        self.iterate_fc()
        if not (value == 'No'):
            if self.on_first():
                self.player.ctrlQ_anonymity_err = value
            return 'The correct answer is  `Not` -- Once you are paired with another participant, ' \
                   'will you NEVER know the identity of the other participant'
        
    def ctrlQ_who_transfers_error_message(self, value):
        self.iterate_fc()
        if not (value == 'Role A'):
            if self.on_first():
                self.player.ctrlQ_who_transfers_err = value

            return 'The correct answer is  `Role A` -- Only Role A can take money from Role B'
        
    def ctrlQ_B_always_sends_error_message(self, value):
        self.iterate_fc()
        if self.group.treatment in ['DM', 'TP']:
            if self.group.value_type == 'WTP' and not (value == 'It depends on his/her valuation for sending a message'):
                if self.on_first():
                    self.player.ctrlQ_B_always_sends_err = value

                return 'The correct answer is  `It depends on his/her valuation for sending a message` : ' \
                       '-- It will be send if the maximum amount willing to pay for sending ' \
                       'the message falls above the message price'
            if self.group.value_type == 'WTA' and not (value == 'It depends on his/her valuation for sending a message'):
                if self.on_first():
                    self.player.ctrlQ_B_always_sends_err = value

                return 'The correct answer is  `It depends on his/her valuation for sending a message` : ' \
                       '-- It will be send if the minimum amount willing to accept for NOT sending ' \
                       'the message falls below the message price'


    def ctrlQ_B_sends_message_error_message(self, value):  # CORRECT WITH PAOLA
        self.iterate_fc()
        if self.group.treatment in ['DM', 'TP']:
            if self.group.value_type == 'WTP' and self.group.elicitation_method == 'BDM' and not (value == 'Yes'):
                if self.on_first():
                    self.player.ctrlQ_B_sends_message_err = value

                return 'The correct answer is  `Yes` -- Because his/her willingness to pay (Y) for sending ' \
                        'is greater than the price of the message (Z)'
            elif self.group.value_type == 'WTP' and self.group.elicitation_method != 'BDM' and not (value == 'Yes'):
                if self.on_first():
                    self.player.ctrlQ_B_sends_message_err = value

                return 'The correct answer is  `Yes` -- Because she/he accepts the amount Z in exchange  ' \
                        'for sending the message'
            if self.group.value_type == 'WTA' and self.group.elicitation_method == 'BDM' and not (value == 'No'):
                if self.on_first():
                    self.player.ctrlQ_B_sends_message_err = value

                return 'The correct answer is  `No` -- Because she/he accepts the amount Z in exchange ' \
                       'for NOT sending the message'
            elif self.group.value_type == 'WTP' and self.group.elicitation_method != 'BDM' and not (value == 'No'):
                if self.on_first():
                    self.player.ctrlQ_B_sends_message_err = value

                return 'The correct answer is  `Yes` -- Because she/he accepts the amount Z in exchange  ' \
                        'for NOT sending the message'

    def ctrlQ_A_earnings_error_message(self, value):
        self.iterate_fc()
        if not (value == '13.00 + X'):
            if self.on_first():
                self.player.ctrlQ_A_earnings_err = value

            return 'The correct answer is `13.00 + X` since A receives an endowment of 3.00, a task income of ' \
                        '10.00 and  took $X from B\'s account. '

    def ctrlQ_B_earnings_error_message(self, value):
        self.iterate_fc()
        if self.group.treatment in ['NM', 'FM']:
            if not (value == '13.00 - X'):
                if self.on_first():
                    self.player.ctrlQ_B_earnings_err = value

                return 'The correct answer is `13.00 - X` since B receives an endowment of 3.00, a task income of ' \
                       '10.00 and Role A took $X from his/her account.'
        if self.group.treatment in ['DM', 'TP']:
            if self.group.value_type == 'WTP' and not (value == '13.00 - X - Z'):
                if self.on_first():
                    self.player.ctrlQ_B_earnings_err = value

                return 'The correct answer is `13.00 - X - Z` since Role B receives an endowment of 3.00, a task income of ' \
                       '10.00, A took $X from his/her account, and a has to pay Z for sending his/her message.'
            if self.group.value_type == 'WTA' and not (value == '13.00 - X + Z'):
                if self.on_first():
                    self.player.ctrlQ_B_earnings_err = value

                return 'The correct answer is `13.00 - X + Z` since Role B receives an endowment of 3.00, a task income ' \
                       'of 10.00, Role A took $X from his/her account, and a compensation Z for NOT sending his/her message.'

    def vars_for_template(self):
        return {
            'recipient': (self.group.treatment == 'DM') * 'the participant in Role A' +
                         (self.group.treatment == 'TP') * 'the Reader',
            'points': self.session.config['USE_POINTS'],
        }

############################################################################################

page_sequence = [
    Instructions,
    ControlQuestions,
]










# form_fields = [
#             'ctrlQ_anonymity',
#             'ctrlQ_who_transfers',
#             'ctrlQ_B_always_sends',
#             'ctrlQ_A_earnings',
#             'ctrlQ_B_sends_message',
#             'ctrlQ_B_earnings'
#         ]
