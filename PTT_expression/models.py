from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)
import random
import json  # ASK MG RLL PVP


author = 'Kristian Lopez Vargas'

doc = """
Your app description
"""

questions = """

- Deal with people not wanting to write any message
    -- two buttons?
    -- ask brit

- css template to increase font-size (morgan)

- [kl] check price calculation in TP

- [kl] text review

- [kl] instructions

- price in tp is zero

- price in dm is too low

- Ask james about new waiting functions

"""


class Constants(BaseConstants):
    name_in_url = 'PTT_expression'
    players_per_group = None
    num_rounds = 1
    max_price_list_size = 20  # in treatments where we use BDM LIST, this is the max number of prices displayed


class Subsession(BaseSubsession):

    # before session
    def before_session_starts(self):

        # number of groups
        num_groups = len(self.session.config['Params'])
        print(num_groups)  # OK

        # group formation
        num_partic = self.session.config['num_demo_participants']  # reads number of participants - CHANGE for PRODUCT
        shuf_players = random.sample(range(1, num_partic + 1), num_partic)  # shuffle order of "players IDs"
        grouping = [shuf_players[i:i + 2] for i in range(0, len(shuf_players), 2)]  # splits "IDs" into 2-sized groups
        self.set_group_matrix(grouping)  # assigns grouping

        # read params and treatments distribution
        i = 0
        for grupo in self.get_groups()[0:num_groups]:  # the slice is because self.get_groups() include a group
            # containing the reader. Reader(s) always comes last
            grupo.treatment = self.session.config['Params'][i]['treat']
            grupo.value_type = self.session.config['Params'][i]['val_typ']
            grupo.elicitation_method = self.session.config['Params'][i]['elic_met']
            grupo.BDM_type = self.session.config['Params'][i]['BDM_typ']
            grupo.endowment = self.session.config['Params'][i]['end']  # this writes a local at group level; used below

            # this loads the parameters of eliciation methods
            grupo.Method_params = self.session.config['Params'][i]['Met_par']
            if grupo.Method_params is not None:
                print(len(grupo.Method_params))
                if len(grupo.Method_params) == 1:
                    grupo.SOP_price = grupo.Method_params[0]
                elif len(grupo.Method_params) == 2:
                    grupo.BDM_lolimit = grupo.Method_params[0]
                    grupo.BDM_uplimit = grupo.Method_params[1]
                elif len(grupo.Method_params) == 3:
                    grupo.BDM_lolimit = grupo.Method_params[0]
                    grupo.BDM_uplimit = grupo.Method_params[1]
                    grupo.BDM_list_step = grupo.Method_params[2]
            i += 1


        # setting message PRICE
        i = 0
        for grupo in self.get_groups()[0:num_groups]:  # the slice is because self.get_groups() include a group
            if grupo.treatment == 'FM':
                grupo.message_price = 0
            elif grupo.treatment == 'NM':
                grupo.message_price = None
            elif grupo.treatment == 'DM' or grupo.treatment == 'TP':
                if len(grupo.Method_params) == 1:  # this is when the price is given in the config, not randomly
                    # generated
                    grupo.message_price = grupo.Method_params[0]
                else:
                    # this sets as upper limit B's endowment -- but if 'av_inc' is set then the maximum random price,
                    # grupo.message_price is determined dynamically after money has been taken and available income is
                    # calculated
                    ul_rnd_price = round(grupo.endowment[1], 2)
                    grupo.message_price = random.randrange(0, 100 * ul_rnd_price) / 100
                    print("random price", grupo.message_price)
            else:
                assert False, " 'treatment' var is incorrectly set in config settings.py"
            i += 1

        # adding treatment to reader 'TP-R'
        for grupo in self.get_groups()[num_groups:num_groups+1]:
            grupo.treatment = 'TP-R'

        # reading endowment from config and write in players model
        for grupo in self.get_groups()[0:num_groups]:
            for player in grupo.get_players():
                player.endowment = grupo.endowment[player.id_in_group-1]

        # reading endowment from config and write in readers field
        for grupo in self.get_groups()[num_groups:num_groups+1]:
            for player in grupo.get_players():
                player.endowment = self.session.config['reader_endowment'][0]



        ### CHECKS ###
        # Check if number of participants in session config is congruent
        assert num_partic == num_groups * 2 + self.session.config['num_readers'], \
            "num_partic != num_groups*2 + num_redrs"

        # Check if when there are TP treats there is a reader too
        treatment_list = []
        num_readers = self.session.config['num_readers']
        for grupo in self.get_groups()[0:num_groups]:
            treatment_list.append(grupo.treatment)
        print("treatment_list", treatment_list)
        assert ('TP' in treatment_list and num_readers >= 1) or ('TP' not in treatment_list and num_readers == 0), \
        "there are tp-groups (reader) and no readers (no tp-groups)"

        # Check if Params in session config is congruent with number of participants
        for grupo in self.get_groups():
            if grupo.treatment == 'DM' or grupo.treatment == 'TP':
                assert grupo.value_type is not None and grupo.elicitation_method is not None and \
                       ((grupo.BDM_type is not None and grupo.BDM_lolimit is not None and grupo.BDM_uplimit)
                        or grupo.SOP_price is not None), \
                "a group in DM or PT does not have the right dictionary in session config"

            elif grupo.treatment == 'NM' or grupo.treatment == 'FM' or grupo.treatment == 'TP-R':
                assert grupo.value_type is None and grupo.elicitation_method is None and \
                       grupo.BDM_type is None and grupo.BDM_lolimit is None and grupo.BDM_uplimit is None and \
                       grupo.SOP_price is None, \
                "a group in NM or FM or TP-R does not have the right dictionary in session config"
            else:
                assert False, "treat in config session contains an unspecified treatment"
            print(grupo, "OK treatment config")

        # transfer vars to participant.vars
        for p in self.get_players():
            p.participant.vars['treatment'] = grupo.treatment
            p.participant.vars['value_type'] = grupo.value_type
            p.participant.vars['elicitation_method'] = grupo.elicitation_method
            p.participant.vars['BDM_type'] = grupo.BDM_type


class Group(BaseGroup):
    # define vars
    take_rate = models.DecimalField(widget=widgets.HiddenInput(), max_digits=5, decimal_places=0, min=0, max=100)
    expected_take_rate = models.DecimalField(widget=widgets.HiddenInput(), max_digits=5, decimal_places=0, min=0, max=100)
    treatment = models.TextField()
    money_taken = models.CurrencyField()
    value_type = models.TextField()
    elicitation_method = models.TextField()
    BDM_type = models.TextField()
    BDM_lolimit = models.TextField()
    BDM_uplimit = models.TextField()
    BDM_list_step = models.DecimalField(max_digits=5, decimal_places=2)
    SOP_price = models.CurrencyField()
    b_message = models.TextField()
    b_value = models.CurrencyField(min=c(0))
    message_price = models.CurrencyField()
    msg_sent = models.BooleanField(initial=0)
    SOP_yes = models.CharField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal())
    price_list = []
    price_list_size = models.IntegerField()
    responses_list = []

    # create vars for timestamps

    time_ADecides = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_BPredicts = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_TakeResults = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_WriteMessage = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    time_AllBdmCont = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_AllBdmList = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_AllSOP = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    time_ElicitBdmCont = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_ElicitBdmList = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_ElicitSOP = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    time_BdmResults = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_DisplayMessageToA = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_DisplayMessagesToR = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    # create BDM List prices - It generates as many variables list_price_{0} as Constants.max_price_list_size
    for i in range(0, Constants.max_price_list_size):
        locals()['list_price_{0}_yes'.format(i)] = models.CharField(choices=['Yes', 'No'],
                                                                    widget=widgets.RadioSelectHorizontal()
                                                                    )

    # this assigns payoff
    def set_payoffs(self):
        for p in self.get_players():
            if p.role() == 'A':
                p.payoff = p.available_income1
            elif p.role() == 'B':
                if p.group.treatment in ['FM', 'NM']:
                    p.payoff = p.available_income1
                elif p.group.treatment in ['DM', 'TP']:
                    p.payoff = p.available_income1 \
                               - (p.group.value_type == 'WTP') * p.group.msg_sent * p.group.message_price \
                               + (p.group.value_type == 'WTA') * (not p.group.msg_sent) * p.group.message_price
            elif p.role() == 'R':
                p.payoff = p.available_income0



class Player(BasePlayer):
    # define vars
    endowment = models.CurrencyField()
    task_income = models.CurrencyField()
    available_income0 = models.CurrencyField()  # before money is taken : endowment plus task income
    others_task_income = models.CurrencyField()
    available_income1 = models.CurrencyField()  # after money is taken : endowment plus task income
    wish_no_message = models.BooleanField(initial='True')
    time_InitialStage2 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_RolesIncome = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_Results = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    # roles
    def role(self):
        if self.id_in_group == 1 and self.group.treatment != 'TP-R':
            return 'A'
        if self.id_in_group == 2 and self.group.treatment != 'TP-R':
            return 'B'
        if self.group.treatment == 'TP-R':
            return 'R'

    # gets the id of partner if you are matched, and of him/herself if the player is the reader
    def get_partner(self):
        if self.role() == 'A' or self.role() == 'B':
            return self.get_others_in_group()[0]
        elif self.role() == 'R':
            return self.group.get_player_by_role('R')  # OJO reader gets as partner him/herself!



###################################











########################################################################################
#'''Draft zone'''

# # read endowment from config
# for player in self.get_players():
#     if 'endowment' in self.session.config:
#         if len(self.session.config['endowment']) == len(self.get_players()):
#             player.endowment = self.session.config['endowment'][player.id_in_group - 1]
#         elif len(self.session.config['endowment']) == 1:
#             player.endowment = self.session.config['endowment'][0]
#         else:
#             assert False, "endowment length is not correct in config file"
#     else:
#         player.target_income = 3

# print(grupo.value_type)

# price list for SOP
# for grupo in self.get_groups()[0:num_groups]:
#     if grupo.elicitation_method == 'SOP':

# group_pages = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'.format(page)}))
# 'InitialWait',
# 'RolesIncome',
# 'ADecides',
# 'BPredicts',
# 'TakeResults',
# 'WriteMessage',
# 'ElicitBdmCont',
# 'ElicitBdmList',
# 'ElicitSOP',
# 'BdmResults',
# 'ElicitSOP',
# 'DisplayMessageToA']
#
# for page in group_pages:
#     print(page)
# 'time_{}'.format(page) = models.TextField(
#     widget=widgets.HiddenInput(attrs={'id': 'time_{}'.format(page)}))
#
# # time_ = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'time_temp'}))


# setting list for BDM List
# max_size = Constants.max_price_list_size
# for grupo in self.get_groups():
#     if grupo.BDM_type == 'LIST':
#         step = c(self.grupo.BDM_list_step)
#         upper_limit = (self.grupo.BDM_uplimit == 'end') * self.player.endowment + \
#                       (self.grupo.BDM_uplimit == 'av_inc') * self.player.available_income1
#         prices = [i * step for i in range(0, max_size - 1)]  # range(0, max_size) has max_size entries, so we take one
#         prices = [p for p in prices if p < upper_limit]
#         prices.append(upper_limit)
#
#         price_list_size = len(prices)
