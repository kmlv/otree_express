from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random
import json
from math import floor

################################################


class InitialWait(WaitPage):

    """ Page 0: wait for partner in group - so income from effort task is read """

    title_text = "Waiting"
    body_text = "Please wait for others to arrive to this stage before you proceed to the next one. Thank you."


class InitialStage2(Page):

    form_model = models.Player
    form_fields = ['time_InitialStage2']

    def before_next_page(self):
        self.player.task_income = self.participant.vars['task_income']
        self.player.available_income0 = self.participant.vars['task_income'] + \
            self.player.endowment


################################################

class RolesIncome(Page):
    """ Page 1: RolesIncome All """
    form_model = models.Player
    form_fields = ['time_RolesIncome']


class ADecides(Page):
    """ Page 2A: A Decides """
    form_model = models.Group
    form_fields = ['take_rate', 'time_ADecides']

    def is_displayed(self):
        return self.player.role() == 'A'

    def vars_for_template(self):
        return {
            'b_task_income': float(self.group.get_player_by_role('B').task_income),
            'b_task_income_': self.group.get_player_by_role('B').task_income,
            'points': self.session.config['USE_POINTS'],
        }

    def before_next_page(self):

        self.group.money_taken = self.group.take_rate / 100 * self.group.get_player_by_role('B').task_income

        for p in self.group.get_players():
            if p.role() == 'A':
                p.available_income1 = p.endowment + p.task_income + self.group.money_taken
            elif p.role() == 'B':
                p.available_income1 = p.endowment + p.task_income - self.group.money_taken
            else:
                assert False, 'there is an error in available incomes'

        # set price when upper limit of BDM is the interim payoff ('av_inc' in configs in settings.py)
        if self.group.BDM_uplimit == 'av_inc':
            ul_rnd_price = round(self.group.get_player_by_id(2).available_income1, 2)
            self.group.message_price = random.randrange(0, 100 * ul_rnd_price) / 100
            print("random price", self.group.message_price)


class BPredicts(Page):
    """Page 2B: B Predicts"""
    form_model = models.Group
    form_fields = ['expected_take_rate', 'time_BPredicts']

    def is_displayed(self):
        return self.player.role() == 'B'

    def vars_for_template(self):
        return {
            'b_task_income':  float(self.group.get_player_by_role('B').task_income) ,
            'points': self.session.config['USE_POINTS'],
        }


class BWaitsForGroup(WaitPage):
    pass
    # def is_displayed(self):
    #     return self.player.role() == 'B'



########################################################################################################################
# Way 1: different pages for receiving info, writing and valuing
#
#
# class TakeResults(Page):  # check: uncomment when running way 1
#     """Page 3: Take Results"""
#     form_model = models.Group
#     form_fields = ['time_TakeResults']
#
#     def is_displayed(self):
#         return self.player.role() == 'A' or self.player.role() == 'B'
#
#
# class WriteMessage(Page):
#     """Page 4: """
#     form_model = models.Group
#     form_fields = ['b_message', 'time_WriteMessage']
#
#     def is_displayed(self):
#         return self.group.treatment == 'FM' and self.player.role() == 'B'
# #        return (self.group.treatment == 'DM' or self.group.treatment == 'TP' or self.group.treatment == 'FM') and \
# #               self.player.role() == 'B'
#
#     def before_next_page(self):
#         if self.group.treatment == 'FM':
#             self.group.msg_sent = True  # this is because FM needs to set msg_sent somewhere
#
#
# class ElicitBdmCont(Page):
#     """Page 5: Elicit BDM - Continuous Value Type"""
#     form_model = models.Group
#     form_fields = ['b_value', 'time_ElicitBdmCont']
#
#     def is_displayed(self):
#         return self.player.role() == 'B' and self.group.elicitation_method == 'BDM' \
#           and self.group.BDM_type == 'CONT'
#
#     def b_value_max(self):
#         return self.player.available_income1
#
#     def b_value_error_message(self, value):
#         if not (0 <= value <= self.player.available_income1):
#             return 'Must be equal or greater than zero and equal or below available income'
#
#     # defining whether message is sent or not
#     def before_next_page(self):
#         # setting boolean whether message is sent or not
#         if self.group.b_value >= self.group.message_price:
#             self.group.msg_sent = True
#         elif self.group.b_value < self.group.message_price:
#             self.group.msg_sent = False
#
#
# class ElicitBdmList(Page):
#     """Page 5: Elicit BDM - List Value Type"""
#
#     def is_displayed(self):
#         return self.player.role() == 'B' and self.group.elicitation_method == 'BDM' \
#                and self.group.BDM_type == 'LIST'
#
#     form_model = models.Group
#
#     def get_form_fields(self):
#         # setting self.group.price_list and self.group.price_list_size so we can set form_fields
#         max_size = Constants.max_price_list_size
#         step = c(self.group.BDM_list_step)
#         upper_limit = (self.group.BDM_uplimit == 'end') * self.player.endowment + \
#                       (self.group.BDM_uplimit == 'av_inc') * self.player.available_income1
#         prices = [i * step for i in
#                   range(0, max_size - 1)]  # range(0, max_size) has max_size entries, so we take one
#         prices = [p for p in prices if p < upper_limit]
#         prices.append(upper_limit)
#         self.group.price_list = prices
#         self.group.price_list_size = len(prices)
#
#         form_fields = ['list_price_{}_yes'.format(i) for i in range(0, self.group.price_list_size)]
#         form_fields.append('time_ElicitBdmList')
#         return form_fields
#
#     def vars_for_template(self):
#         return {
#             'prices': self.group.price_list
#         }
#
#     # defining b values and whether message is sent or not
#     def before_next_page(self):
#
#         # reading responses and putting them in a list
#         responses_list = []
#         for i in range(0, self.group.price_list_size):
#             # res = getattr(self.group, 'list_price_{}_yes'.format(i))
#             responses_list.append(getattr(self.group, 'list_price_{}_yes'.format(i)))
#             print(responses_list)
#
#         # WTP: value is highest price to which player b says Yes
#         if self.group.value_type == 'WTP':
#             if 'Yes' in responses_list:
#                 posit = len(responses_list) - 1 - responses_list[::-1].index(
#                     'Yes')  # finds last occurrence of Yes
#                 self.group.b_value = self.group.price_list[posit]
#             else:
#                 self.group.b_value = 0
#                 print("b_value", self.group.b_value)
#
#         # WTA: value is highest price to which player b says No
#         if self.group.value_type == 'WTA':
#             if 'No' in responses_list:
#                 posit = len(responses_list) - 1 - responses_list[::-1].index(
#                     'No')  # finds last occurrence of No
#                 self.group.b_value = self.group.price_list[posit]
#             else:
#                 self.group.b_value = 0
#         print("b_value", self.group.b_value)
#
#         # random price in BDM list needs to be an element of price list (try with two groups with different price lists)
#         if self.group.BDM_type == 'LIST':
#             self.group.message_price = min(self.group.price_list,
#                                            key=lambda x: abs(x - self.group.message_price))
#
#         # setting boolean whether message is sent or not
#         if self.group.b_value >= self.group.message_price:
#             self.group.msg_sent = True
#         elif self.group.b_value < self.group.message_price:
#             self.group.msg_sent = False
#
#
# class ElicitSOP(Page):
#     """Page _:"""
#     form_model = models.Group
#     form_fields = ['SOP_yes', 'time_ElicitSOP']
#
#     def is_displayed(self):
#        return self.player.role() == 'B' and self.group.elicitation_method == 'SOP'
#
#     def before_next_page(self):
#
#         # if self.group.treatment == 'FM':
#         #     self.group.msg_sent = True  # setting boolean whether message is sent or not
#         # else:
#
#         if self.group.value_type == 'WTP':
#             if self.group.SOP_yes == 'Yes':
#                 self.group.msg_sent = True
#             elif self.group.SOP_yes == 'No':
#                 self.group.msg_sent = False
#
#         if self.group.value_type == 'WTA':
#             if self.group.SOP_yes == 'Yes':
#                 self.group.msg_sent = False
#             elif self.group.SOP_yes == 'No':
#                 self.group.msg_sent = True


########################################################################################################################
# Way 2: ONE page for receiving info, writing and valuing


class TakeResults(Page):
    """Take Results"""
    form_model = models.Group
    form_fields = ['time_TakeResults']

    def is_displayed(self):
        return self.player.role() == 'A'  # because these results are given in new pages AllBdmList, AllBdmCont, or AllSOP.


class AllBdmCont(Page):

    form_model = models.Group
    form_fields = ['b_value',  'b_message', 'time_AllBdmCont']

    def is_displayed(self):
        return (self.group.treatment == 'DM' or self.group.treatment == 'TP' or self.group.treatment == 'FM') and \
              self.player.role() == 'B' and self.group.elicitation_method == 'BDM' \
              and self.group.BDM_type == 'CONT'

    def b_value_max(self):
       return self.player.available_income1

    def b_value_error_message(self, value):
        if not (0 <= value <= self.player.available_income1):
           return 'Must be equal or greater than zero and equal or below available income'

    # defining whether message is sent or not
    def before_next_page(self):
        if self.group.treatment == 'FM':
           self.group.msg_sent = True  # this is because FM needs to set msg_sent somewhere
        else:
           self.group.msg_sent = False
        # setting boolean whether message is sent or not
        if self.group.b_value >= self.group.message_price:
           self.group.msg_sent = True
        elif self.group.b_value < self.group.message_price:
           self.group.msg_sent = False

class AllBdmList(Page):
    form_model = models.Group

    def get_form_fields(self):
           # setting self.group.price_list and self.group.price_list_size so we can set form_fields
        max_size = Constants.max_price_list_size
        step = c(self.group.BDM_list_step)
        upper_limit = (self.group.BDM_uplimit == 'end') * self.player.endowment + \
                     (self.group.BDM_uplimit == 'av_inc') * self.player.available_income1
        prices = [i * step for i in range(0, max_size - 1)]  # range(0, max_size) has max_size entries, so we take one
        prices = [p for p in prices if p < upper_limit]
        prices.append(upper_limit)
        self.group.price_list = prices
        self.group.price_list_size = len(prices)

        form_fields = ['list_price_{}_yes'.format(i) for i in range(0, self.group.price_list_size)]
        form_fields.append('b_message')
        form_fields.append('time_AllBdmList')
        return form_fields

    def vars_for_template(self):
        return {
           'prices': self.group.price_list
        }

    def is_displayed(self):
        return (self.group.treatment == 'DM' or self.group.treatment == 'TP' or self.group.treatment == 'FM') and \
              self.player.role() == 'B' and self.group.elicitation_method == 'BDM' and self.group.BDM_type == 'LIST'

    # defining b values and whether message is sent or not
    def before_next_page(self):
        if self.group.treatment == 'FM':
            self.group.msg_sent = True  # this is because FM needs to set msg_sent somewhere
        else:
            self.group.msg_sent = False
        # reading responses and putting them in a list
        responses_list = []
        for i in range(0, self.group.price_list_size):
            res = getattr(self.group, 'list_price_{}_yes'.format(i))
            responses_list.append(getattr(self.group, 'list_price_{}_yes'.format(i)))
        print(responses_list)

        # WTP: value is highest price to which player b says Yes
        if self.group.value_type == 'WTP':
            if 'Yes' in responses_list:
                posit = len(responses_list) - 1 - responses_list[::-1].index('Yes')  # finds last occurrence of Yes
                self.group.b_value = self.group.price_list[posit]
            else:
                self.group.b_value = 0
        print("b_value", self.group.b_value)

        # WTA: value is highest price to which player b says No
        if self.group.value_type == 'WTA':
            if 'No' in responses_list:
                posit = len(responses_list) - 1 - responses_list[::-1].index('No')  # finds last occurrence of No
                self.group.b_value = self.group.price_list[posit]
            else:
                self.group.b_value = 0
        print("b_value", self.group.b_value)

        # Paola agreaga una var que indica consistencia: 1 consistente 0 inconsistente
        # random price in BDM list needs to be an element of price list (try with two groups with different price lists)

        if self.group.BDM_type == 'LIST':
            self.group.message_price = min(self.group.price_list, key=lambda x: abs(x - self.group.message_price))

        # setting boolean whether message is sent or not
        if self.group.b_value >= self.group.message_price:
            self.group.msg_sent = True
        elif self.group.b_value < self.group.message_price:
            self.group.msg_sent = False


# class AllSOP(Page):
#    """Page _:"""
#    form_model = models.Group
#    form_fields = ['SOP_yes', 'b_message', 'time_AllSOP']
#
#    def is_displayed(self):
#        return (self.group.treatment == 'DM' or self.group.treatment == 'TP' or self.group.treatment == 'FM') and \
#               self.player.role() == 'B' and self.group.elicitation_method == 'SOP'
#
#    def before_next_page(self):
#        if self.group.treatment == 'FM':
#            self.group.msg_sent = True  # setting boolean whether message is sent or not
#        else:
#            self.group.msg_sent = False
#        if self.group.value_type == 'WTP':
#            if self.group.SOP_yes == 'Yes':
#                self.group.msg_sent = True
#            elif self.group.SOP_yes == 'No':
#                self.group.msg_sent = False
#
#        if self.group.value_type == 'WTA':
#            if self.group.SOP_yes == 'Yes':
#                self.group.msg_sent = False
#            elif self.group.SOP_yes == 'No':
#                self.group.msg_sent = True


########################################################################################################################
# Continues with rest of pages


class BdmResults(Page):
    """Page _:"""
    form_model = models.Group
    form_fields = ['time_BdmResults']

    def is_displayed(self):
        return self.player.role() == 'B' and self.group.elicitation_method == 'BDM'


class AWaitsForGroup(WaitPage):
    pass
    # def is_displayed(self):
    #     return self.player.role() == 'A'


class DisplayMessageToA(Page):
    """Page _: message is shown to player A"""
    form_model = models.Group
    form_fields = ['time_DisplayMessageToA']

    def is_displayed(self):
        return self.player.role() == 'A' and self.group.msg_sent and \
               (self.group.treatment == 'DM' or self.group.treatment == 'FM')


class WaitMessagesInTP(WaitPage):
    """ Page _: Reader Waits for B\TP players messages """
    wait_for_all_groups = True  # for whom x needs to wait

    # x who he/she waits
    def is_displayed(self):
        return self.player.role() == 'R'


class DisplayMessagesToR(Page):
    """Page _: Reader reads messages from B players"""

    form_model = models.Group
    form_fields = ['time_DisplayMessagesToR']

    def is_displayed(self):
        return self.player.role() == 'R'

    def vars_for_template(self):
        msg_list = []
        for group in self.subsession.get_groups():
            if group.treatment == 'TP' and group.msg_sent:
                msg_list.append(group.b_message)
        if not msg_list:  # this uses that `not []' returns True
            msg_list = ['None of the B players sent messages for you to read']
        return {
            'msg_list': msg_list
        }


class ResultsWaitPage(WaitPage):
    """Page_: wait for other in group to calc payoffs and show results """

    def after_all_players_arrive(self):
        self.group.set_payoffs()


class Results(Page):
    """Page _: Page hosws table of final earnings"""
    form_model = models.Player
    form_fields = ['time_Results']

    def vars_for_template(self):

        if 'R' in self.player.role():  # otherwise otree complains that there is no R player
            p_r = self.group.get_player_by_role('R')
            return {
                'R_endowment': p_r.endowment,
                'R_task_income': p_r.task_income,
                'R_payoff': p_r.payoff
            }
        if 'A' or 'B' in self.player.role():  # otherwise otree complains that there is no R player
            p_a = self.group.get_player_by_role('A')
            p_b = self.group.get_player_by_role('B')
            return {
                'A_endowment': p_a.endowment,
                'B_endowment': p_b.endowment,
                'A_task_income': p_a.task_income,
                'B_task_income': p_b.task_income,
                'A_payoff': p_a.payoff,
                'B_payoff': p_b.payoff,
                'points': self.session.config['USE_POINTS'],
            }


## defines page sequence
page_sequence = [
    InitialWait,
    InitialStage2,
    RolesIncome,
    BPredicts,
    ADecides,
    BWaitsForGroup,
    TakeResults,
    # B waits for A's decision
    # WriteMessage,
    # ElicitBdmCont,
    # ElicitBdmList,
    # ElicitSOP,
    AllBdmCont,
    AllBdmList,
    # AllSOP,
    AWaitsForGroup,  # A waits for possible message
    BdmResults,
    DisplayMessageToA,
    WaitMessagesInTP,
    DisplayMessagesToR,
    ResultsWaitPage,
    Results
]

##############################################
## DRAFT ZONE

# def is_displayed(self):
#     return self.player.id_in_group == 2 and self.group.treatment != 'TP-R'

# record responses in a list
# responses_list = []
# for i in range(0, self.group.price_list_size):
#     responses_list.append(locals()['price{}'.format(i)])
# print(responses_list)


# this repetitive code is what we need to correct with the appropriate use of for, locals(), and
# self.group.list_price_size
# the code below will break if the list_price_size has less than 20 entries
# price0 = self.group.list_price_0_yes
# price1 = self.group.list_price_1_yes
# price2 = self.group.list_price_2_yes
# price3 = self.group.list_price_3_yes
# price4 = self.group.list_price_4_yes
# price5 = self.group.list_price_5_yes
# price6 = self.group.list_price_6_yes
# price7 = self.group.list_price_7_yes
# price8 = self.group.list_price_8_yes
# price9 = self.group.list_price_9_yes
# price10 = self.group.list_price_10_yes
# price11 = self.group.list_price_11_yes
# price12 = self.group.list_price_12_yes
# price13 = self.group.list_price_13_yes
# price14 = self.group.list_price_14_yes
# price15 = self.group.list_price_15_yes
# price16 = self.group.list_price_16_yes
# price17 = self.group.list_price_17_yes
# price18 = self.group.list_price_18_yes
# price19 = self.group.list_price_19_yes  # starts in 0

# # setting boolean whether message is sent or not
# if (self.group.value_type == 'WTP' and self.group.b_value >= self.group.message_price) or \
#         (self.group.value_type == 'WTA' and self.group.b_value <= self.group.message_price):
#     self.group.msg_sent = True
# elif (self.group.value_type == 'WTP' and self.group.b_value < self.group.message_price) or \
#         (self.group.value_type == 'WTA' and self.group.b_value > self.group.message_price):
#     self.group.msg_sent = False


# assert False, "my stop"

# locals()['price{}'.format(i)]
#      self.group.responses_list.append(res)
#
# locals()['self.group.list_price_{}_yes'.format(i)]
# # #     self.group.responses_list.append(res)


# assert False, "my stop"

# print(self.group.list_price_14_yes)
#
# print(locals()['temp{}'.format(14)])

# if self.group.value_type == 'WTP':
#     # i = self.group.price_list_size
#     # self.group.b_value = 0
#     for i in range(self.group.price_list_size, 0, -1):
#         print(locals()['list_price_{}_yes'.format(i)])


# price0 = self.group.list_price_0_yes
#
# for i in range(0, self.group.price_list_size):
#     locals()['price{}'.format(i)] = locals()['self.group.list_price_{0}_yes'.format(i)]
# print(locals())


#
# if self.group.value_type == 'WTP':
#     if 1 in responses:
#         posit = len(responses) - 1 - responses[::-1].index(1)  # finds last occurrence of 1
#         self.group.b_value = self.group.price_list[posit]
#     else:
#         self.group.b_value = 0
#
# print("b_value")
# print(self.group.b_value)
#
# if self.group.value_type == 'WTA':
#     if 1 in responses:
#         posit = responses.index(1)
#         self.group.b_value = self.group.price_list[posit]
#     else:
#         self.group.b_value = 0
#
# # setting boolean whether message is sent or not
# if (self.group.value_type == 'WTP' and self.group.b_value >= self.group.message_price) or \
#         (self.group.value_type == 'WTA' and self.group.b_value <= self.group.message_price):
#     self.group.msg_sent = True
# elif (self.group.value_type == 'WTP' and self.group.b_value < self.group.message_price) or \
#         (self.group.value_type == 'WTA' and self.group.b_value > self.group.message_price):
#     self.group.msg_sent = False


#
# self.group.tempVAR_0 = 0
# self.group.tempVAR_1 = 0
# self.group.tempVAR_2 = 1
#
# # for i in range(0, 3):
# print('test', self.group.tempVAR_2)
# ttt = locals()['self.group.tempVAR_{}'.format(0)]
# print(ttt)
# self.group.responses_list = self.group.responses_list.append(ttt)
# print(self.group.responses_list)
#
# # for i in range(0, self.group.price_list_size):
# #     self.group.responses_list = locals()['self.group.list_price_{}_yes'.format(i)]
# #     self.group.responses_list.append(res)
#
#
# # print("count", i)
# # print(self.group.list_price_14_yes)
# # temp1 = 'self.group.list_price_{}_yes'.format(i)
# # temp = self.group.temp1
# # print(temp)
# # #
# # pr = locals()['self.group.list_price_{}_yes'.format(i)]
# #
# # responses.append(pr)
#
# assert False, "stop"


# 'range': range(1, 20+1)
# 'price_fields': list(form),
# 'price_fields': ['group.list_price_{}_yes'.format(i) for i in range(1, 20)]
# from manual
# form_model = models.Player
# def get_form_fields(self):
#     return ['contribution_{}'.format(i) for i in range(1, self.player.n + 1)]

# for gg in self.subsession.get_groups():
#     print(gg)
#     if gg.treatment == 'TP':
#         print(gg.b_message)
#         print(self.subsession.reader_messages)
#         print(type(self.subsession.reader_messages))
#         temp = self.subsession.reader_messages
#         self.subsession.reader_messages = temp.append(gg.b_message)
#         msg_list = [self.subsession.reader_messages, gg.b_message]
#         print(msg_list)
#         self.subsession.reader_messages = ' ;; '.join(msg_list)


# def vars_for_template(self):
#     return {
#         'reader_messages': self.subsession.reader_messages
#     }

# # Ask Raul or Morgan
# def vars_for_template(self):
#     jsonDec = json.decoder.JSONDecoder()
#     messages_list = jsonDec.decode(self.subsession.reader_message)
#     return {
#         'messages': messages_list[self.player.id_in_group - 1],
#         'allMessages': messages_list
#     }
# call task_income and available_income from config
# def vars_for_template(self):
#     return {
#             'partner': self.player.get_partner(),
#             'task_income': self.participant.vars['task_income'],
#             'available_income': self.participant.vars['task_income']+self.player.endowment,
#             'others_task_income': self.player.get_partner().task_income
#             }


# def get_form_fields(self):
#     # this is because BDM_uplimit comes from config file
#     upper_limit = (self.group.BDM_uplimit == 'end') * self.player.endowment + \
#                   (self.group.BDM_uplimit == 'av_inc') * self.player.available_income1
#     # if the step is too small it will only generate 20 prices.
#     price_list_size = min(20, floor(upper_limit / self.group.BDM_list_step) + 2 -
#                           (upper_limit % self.group.BDM_list_step == 0))
#     print(upper_limit / self.group.BDM_list_step)
#     print(upper_limit % self.group.BDM_list_step == 0)
#     print(price_list_size)
#     form_fields = ['list_price_{}_yes'.format(i) for i in range(1, price_list_size + 1)]
#     form_fields.append('time_ElicitBdmList')
#     print(form_fields)
#     return form_fields

# value set to the max price for wich the player decides to buy
#

# if upper_limit % step == 0:
# elif upper_limit % step > 0:
#     price_list_size = min(20, floor(upper_limit / upper_limit) + 2)
#     prices = [i * step for i in range(0, price_list_size)]
#     prices.append(upper_limit)
#     return {
#         'prices': prices
#     }


# def vars_for_template(self):
#     step = self.group.BDM_list_step
#     print(step)
#     return {
#         'prices': [i * step for i in range(0, 17)],
#         'number_prices': range(1, 17 + 1)
#     }

###########################################
# def get_form_fields(self):
#     form_fields = ['list_price_{0}_yes'.format(i) for i in range(1, 20 + 1)]
#     form_fields.append('time_ElicitBdmList')
#     return form_fields
#
# def vars_for_template(self):
#     step = self.group.BDM_list_step
#     print(step)
#     return {
#         'prices': [i * step for i in range(0, 20)],
#         'number_prices': range(1, 20 + 1)
#     }
#
#
#
##########################################

# form_fields = ['list_price_{}_yes'.format(i) for i in range(1, 20 + 1)]
# form_fields.append('time_ElicitBdmList')
# print(form_fields)



# def get_form_fields(self):
#     # if the step is too small it will only generate 20 prices.
#     upper_limit = (self.group.BDM_uplimit == 'end')*self.player.endowment + \
#                   (self.group.BDM_uplimit == 'av_inc')*self.player.available_income1
#     price_list_size = min(20,  floor(upper_limit / self.group.BDM_list_step) + 2 -
#                                     (upper_limit % self.group.BDM_list_step == 0))
#     print(upper_limit / self.group.BDM_list_step)
#     print(upper_limit % self.group.BDM_list_step == 0)
#     print(price_list_size)
#     form_fields = ['list_price_{}_yes'.format(i) for i in range(1, price_list_size + 1)]
#     form_fields.append('time_ElicitBdmList')
#     print(form_fields)
#     return form_fields.append('time_ElicitBdmList')
#
# def vars_for_template(self):
#     step = self.group.BDM_list_step
#     return {
#         'prices': [i * step for i in range(0, 17)],
#         'number_prices': range(1, 17 + 1)
#     }

# step = self.group.BDM_list_step
# if self.player.available_income1 % self.group.BDM_list_step == c(0):
#     price_list_size = min(20, floor(self.player.available_income1 / self.group.BDM_list_step)) + 1
#     return {
#         'prices': [i * step for i in range(0, price_list_size + 1)]
#     }
# if self.player.available_income1 % self.group.BDM_list_step > c(0):
#     price_list_size = min(20, floor(self.player.available_income1 / self.group.BDM_list_step)) + 2
#     return {
#         'prices': [i * step for i in range(0, price_list_size + 1)].append(self.player.available_income1)
#     }

# def vars_for_template(self):
#     step = self.group.BDM_list_step
#     if self.player.available_income1 % self.group.BDM_list_step == 0:
#         price_list_size = min(20, floor(self.player.available_income1 / self.group.BDM_list_step)) + 1
#         return {
#             'prices': [i * step for i in range(0, price_list_size+1)],
#         }
#     if self.player.available_income1 % self.group.BDM_list_step > 0:
#         price_list_size = min(20, floor(self.player.available_income1 / self.group.BDM_list_step)) + 2
#         return {
#             'prices': [i * step for i in range(0, price_list_size+1)].append(self.player.available_income1),
#         }


# if self.player.available_income1 % self.group.BDM_list_step == 0:
#
#
#     return {
#         'prices': [i * step for i in range(0, 20)],
#         'number_prices': range(1, 20 + 1)
#     }
# elif self.player.available_income1 % self.group.BDM_list_step != 0:
#     step = self.group.BDM_list_step
#     price_list_size = min(20, floor(self.player.available_income1 / self.group.BDM_list_step) + 2
#     return {
#         'prices': [i * step for i in range(0, 20)].append(self.player.available_income1),
#         'number_prices': range(1, 20 + 2)
#     }


# add message to list of reader messages
# def before_next_page(self):
#     self.subsession.reader_messages = ['0']
#     for gg in self.subsession.get_groups():
#         print(gg)
#         if gg.treatment == 'TP':
#             print(gg.b_message)
#             print(self.subsession.reader_messages)
#             print(type(self.subsession.reader_messages))
#             temp = self.subsession.reader_messages
#             self.subsession.reader_messages = temp.append(gg.b_message)
#             msg_list = [self.subsession.reader_messages, gg.b_message]
#             print(msg_list)
#             self.subsession.reader_messages = ' ;; '.join(msg_list)


# messages = [self.subsession.reader_messages]
# self.subsession.reader_messages = messages.append(self.group.b_message)

# # add message to list of reader messages # ASK RAUL
# def before_next_page(self):
#     jsonDec = json.decoder.JSONDecoder()
#     messages_list = jsonDec.decode(self.subsession.reader_message)
#     print(messages_list)
#     reader = self.group.reader_index - 1
#
#     messages_list[reader].append(self.group.b_message)
#     print(messages_list)
#     print(messages_list[reader])
#     self.subsession.reader_message = json.dumps(messages_list)
#     print(self.subsession.reader_message)


# if (self.group.value_type == 'WTP' and self.group.b_value >= self.group.message_price) or \
#         (self.group.value_type == 'WTA' and self.group.b_value >= self.group.message_price):
#     self.group.msg_sent = True
# elif (self.group.value_type == 'WTP' and self.group.b_value < self.group.message_price) or \
#         (self.group.value_type == 'WTA' and self.group.b_value < self.group.message_price):
#     self.group.msg_sent = False
