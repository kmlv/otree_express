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
"""


class Constants(BaseConstants):
    name_in_url = 'PTT_expression'
    players_per_group = None
    num_rounds = 1
    # in treatments where we use BDM LIST, this is the max number of prices displayed
    max_price_list_size = 20


class Subsession(BaseSubsession):

    # before session
    def before_session_starts(self):

        # typical config dictionary
        # 'Params': [
        #     {'treat': 'TP', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'end'],      'end': [3, 3]},
        #     {'treat': 'TP', 'val_typ': 'WTP', 'elic_met': 'BDM', 'BDM_typ': 'LIST', 'Met_par': [0, 'end', 0.5], 'end': [3, 3]},
        #     {'treat': 'TP', 'val_typ': 'WTA', 'elic_met': 'BDM', 'BDM_typ': 'CONT', 'Met_par': [0, 'av_inc'],   'end': [3, 3]},
        # ]

        # number of groups
        num_groups = len(self.session.config['Params'])
        print(num_groups)  # OK

        # group formation
        # reads number of participants - CHANGE for PRODUCT
        num_partic = self.session.config['num_demo_participants']
        # shuf_players = random.sample(range(1, num_partic + 1), num_partic)  # shuffle order of "players IDs"
        shuf_players = random.sample(
            [i for i in range(1, num_partic + 1)], num_partic)

        # shuf_players = random.sample(range(1, num_partic), num_partic - 1) # shuffle order of "players IDs"
        # shuf_players.append(num_partic)
        # shuf_players = range(1, num_partic + 1)  # shuffle order of "players IDs"

        # shuf_players = [i for i in range(1, num_partic + 1)]
        # swap player 11 to last spot
        # participant_labels = [p.participant.label for p in self.get_players()]
        # print(participant_labels)
        # try:
        #     p11_id = participant_labels.index('LEEPS_11') + 1
        #     swap_player = shuf_players[-1]
        #     shuf_players[shuf_players.index(p11_id)] = swap_player
        #     shuf_players[-1] = p11_id
        # except ValueError:
        #     print ('excepted')
        #     pass

        # splits "IDs" into 2-sized groups
        grouping = [shuf_players[i:i + 2]
                    for i in range(0, len(shuf_players), 2)]
        print("XXXXX")
        print(grouping)
        print(self.get_group_matrix())
        print('XXXXX')
        self.set_group_matrix(grouping)  # assigns grouping

        # read params and treatments distribution
        i = 0
        # the slice is because self.get_groups() include a group
        for grupo in self.get_groups()[0:num_groups]:
            # if self.session.config['Params'][i]['treat'] == 'DIS':
            #    grupo.discard = True
            #    grupo.treatment = 'DM'
            # containing the reader. Reader(s) always comes last
            # else:
            grupo.treatment = self.session.config['Params'][i]['treat']
            # grupo.discard = 'discard' in self.session.config['Params'][i]
            grupo.value_type = self.session.config['Params'][i]['val_typ']
            grupo.elicitation_method = self.session.config['Params'][i]['elic_met']
            grupo.BDM_type = self.session.config['Params'][i]['BDM_typ']

            # this writes a local at group level; used below
            grupo.endowment = self.session.config['Params'][i]['end']

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

            # create BDM List compensations - It generates as many variables list_price_{0} as Constants.max_price_list_size
        # for i in range(0, Constants.max_price_list_size): # code taken from allbdmlist in views
         #   locals()['list_compensation_{0}'.format(i)] = models.CharField(choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank = True)
            # create BDM List prices - It generates as many variables list_price_{0} as Constants.max_price_list_size

        # for i in range(0, Constants.max_price_list_size):
         #   locals()['list_price_{0}_yes'.format(i)] = models.CharField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank = True)

        # setting message PRICE
        i = 0
        # the slice is because self.get_groups() include a group
        for grupo in self.get_groups()[0:num_groups]:

            if grupo.treatment == 'FM':
                grupo.message_price = 0
            elif grupo.treatment == 'NM':
                grupo.message_price = None
            # elif grupo.treatment == 'DCM':
            #     grupo.discard = True
            elif grupo.treatment == 'DM' or grupo.treatment == 'TP' or grupo.treatment == 'DIS':

                # this is when the price is given in the config, not randomly
                if len(grupo.Method_params) == 1:
                    # generated
                    grupo.message_price = grupo.Method_params[0]
                else:
                    # this sets as upper limit B's endowment -- but if 'av_inc' is set then the maximum random price,
                    # grupo.message_price is determined dynamically after money has been taken and available income is
                    # calculated
                    ul_rnd_price = round(grupo.endowment[1], 2)
                    grupo.message_price = random.randrange(
                        0, 100 * ul_rnd_price) / 100
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
                player.participation_fee = player.session.config['participation_fee']

        # reading endowment from config and write in readers field
        for grupo in self.get_groups()[num_groups:num_groups+1]:
            for player in grupo.get_players():
                player.endowment = self.session.config['reader_endowment'][0]
                player.participation_fee = player.session.config['participation_fee']

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

            if grupo.treatment == 'DIS' or grupo.treatment == 'DM' or grupo.treatment == 'TP':
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

        # check if BDM LIST => len met_par == 3, if BDM CONT len met_par < 3
        for grupo in self.get_groups():
            if grupo.treatment == 'DM' or grupo.treatment == 'DIS' or grupo.treatment == 'TP'and grupo.elicitation_method == 'BDM':
                if grupo.BDM_type == 'LIST':
                    assert len(
                        grupo.Method_params) == 3, 'BDM LIST requires len(Met_par)==3 in config'
                elif grupo.BDM_type == 'CONT':
                    assert len(
                        grupo.Method_params) < 3, 'BDM CONT requires len(Met_par)==3 in config'

        ## SEARCH TASK SUBSESSION LOGIC
        self.debug_mode = self.session.config['debug']
        for person in self.get_players():
            if 'targetIncome' in self.session.config:
                if len(self.session.config['targetIncome']) == len(self.get_players()):
                    person.target_income = self.session.config['targetIncome'][person.id_in_group - 1]
                elif len(self.session.config['targetIncome']) == 1:
                    person.target_income = self.session.config['targetIncome'][0]
                else:
                    assert False, 'targetIncome is not set properly'
            else:
                person.target_income = 10  # default value
            if 'maxScreens' in self.session.config:
                person.maxScreens = self.session.config['maxScreens']
            else:
                person.maxScreens = 20
            if 'screenTime' in self.session.config:
                person.screenTime = self.session.config['screenTime']
            else:
                person.screenTime = 20
            if 'pointDistMin' in self.session.config:
                person.pointDistMin = self.session.config['pointDistMin']
            else:
                person.pointDistMin = 20
            if 'pointDistMax' in self.session.config:
                person.pointDistMax = self.session.config['pointDistMax']
            else:
                person.pointDistMax = 100




class Group(BaseGroup):
    # define vars

    a_task_income = models.DecimalField(max_digits=5, decimal_places=2)
    b_task_income = models.CurrencyField()
    discard = models.BooleanField()

    treatment = models.TextField()
    value_type = models.TextField()
    elicitation_method = models.TextField()
    BDM_type = models.TextField()
    BDM_lolimit = models.TextField()
    BDM_uplimit = models.TextField()
    BDM_list_step = models.DecimalField(max_digits=5, decimal_places=2)
    SOP_price = models.CurrencyField()

    take_rate = models.DecimalField(
        widget=widgets.HiddenInput(), max_digits=5, decimal_places=0, min=0, max=100)
    expected_take_rate = models.DecimalField(
        widget=widgets.HiddenInput(), max_digits=5, decimal_places=0, min=0, max=100)
    money_taken = models.CurrencyField()
    want_send_message = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)

    b_message = models.TextField(blank=True, initial="")
    b_value = models.CurrencyField(min=c(0), blank=True)

    message_price = models.CurrencyField()
    msg_sent = models.BooleanField(initial=0)
    SOP_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal())

    price_list_size = models.IntegerField()
    # below code moved to before session starts
    '''
    # create BDM List prices - It generates as many variables list_price_{0} as Constants.max_price_list_size
    for i in range(0, Constants.max_price_list_size):
        locals()['list_price_{0}_yes'.format(i)] = models.CharField(
            choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank = True)

    # create BDM compensation amount - It generates as many variables list_price_{0} as Constants.max_price_list_size
    for i in range(0, Constants.max_price_list_size):
        locals()['list_compensation_{0}'.format(i)] = models.CharField(choices=[
               'Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank = True)
    '''
    # low tech solutions because the for loops wouldn't work
    list_price_0_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_1_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_2_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_3_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_4_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_5_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_6_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_7_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_8_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_9_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_10_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_11_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_12_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_13_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_14_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_15_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_16_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_17_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_18_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_price_19_yes = models.CharField(
        choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(), blank=True)

    list_compensation_0 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_1 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_2 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_3 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_4 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_5 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_6 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_7 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_8 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_9 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_10 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_11 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_12 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_13 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_14 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_15 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_16 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_17 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_18 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)
    list_compensation_19 = models.CharField(
        choices=['Send message', 'Receive'], widget=widgets.RadioSelectHorizontal(), blank=True)

    # create vars for timestamps
    time_ADecides = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_BPredicts = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_ATakeResults = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    # time_BTakeResults = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    # time_WriteMessage = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    time_AllFmNm = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_AllBdmCont = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_AllBdmList = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_AllSOP = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    # time_ElicitBdmCont = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    # time_ElicitBdmList = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    # time_ElicitSOP = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    time_BdmResults = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_DisplayMessageToA = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_DisplayMessagesToR = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    # this assigns payoff
    def set_payoffs(self):
        for p in self.get_players():
            if p.role() == 'A':
                p.payoff = p.available_income1
            elif p.role() == 'B':
                if p.group.treatment in ['FM', 'NM']:
                    p.payoff = p.available_income1
                elif p.group.treatment in ['DM', 'TP', 'DIS']:
                    p.payoff = p.available_income1 \
                        - (p.group.value_type == 'WTP') * p.group.msg_sent * p.group.message_price \
                        + (p.group.value_type == 'WTA') * \
                        (not p.group.msg_sent) * \
                        p.group.message_price
            elif p.role() == 'R':
                p.payoff = p.available_income0


class Player(BasePlayer):
    # define vars
    endowment = models.CurrencyField()
    participation_fee = models.CurrencyField()

    task_income = models.CurrencyField()
    # before money is taken : endowment plus task income
    available_income0 = models.CurrencyField()
    # after money is taken : endowment plus task income
    number_of_questions = models.IntegerField(initial=6)
    fields_checked = models.IntegerField(initial=-1)
    available_income1 = models.CurrencyField()
    time_Instructions = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_ControlQuestions = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_InitialStage2 = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_RolesIncome = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_Results = models.TextField(
        widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

        ## PTT EXPRESS INSTRUCTIONS FIELDS
    ctrlQ_anonymity = models.CharField(
        verbose_name='Once you are paired with another participant, '
                     'will you ever know the identity of this other participant?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelectHorizontal())

    ctrlQ_anonymity_err = models.CharField(
        choices=['Yes', 'No'])

    ctrlQ_who_transfers = models.CharField(
        verbose_name='Who decides how much to take from Role B’s account and deposit it into Role A’s account?',
        choices=['Role A', 'Role B', 'Role C', 'Role R', 'None of the above'],
        widget=widgets.RadioSelect())

    ctrlQ_who_transfers_err = models.CharField(
        choices=['Role A', 'Role B', 'Role C', 'Role R', 'None of the above'])

    ctrlQ_B_always_sends = models.CharField(
        verbose_name='Will the participant in Role B always send a message to the participant in Role A '
                     'that he/she is matched with?',
        choices=['Yes', 'No',
                 'It depends on his/her valuation for sending a message'],
        widget=widgets.RadioSelect())

    ctrlQ_B_always_sends_err = models.CharField(
        choices=['Yes', 'No', 'It depends on his/her valuation for sending a message'])

    ctrlQ_B_sends_message = models.CharField(
        verbose_name='Will the message written by Role B be sent in this case?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelectHorizontal())

    ctrlQ_B_sends_message_err = models.CharField(
        choices=['Yes', 'No'])

    # labels are going to be defying directly in ControlQuestions.html file instead of verbose
    ctrlQ_A_earnings = models.CharField(
        #        verbose_name='What are the final earnings for the participant in Role A? '
        #                     '(Hints: endowment plus task income equals $13.00. Do not include participation fee)',
        choices=['13.00 + X', '13.00 - X', '13.00 - X - Z', '13.00 - X + Z'],
        widget=widgets.RadioSelect())

    ctrlQ_A_earnings_err = models.CharField(
        choices=['13.00 + X', '13.00 - X', '13.00 - X - Z', '13.00 - X + Z'])

    ctrlQ_B_earnings = models.CharField(
        #        verbose_name='What are the final earnings for the participant in Role B? '
        #                    '(Hints: endowment plus task income equals $13.00. Do not include participation fee)',
        choices=['13.00 + X', '13.00 - X', '13.00 - X - Z', '13.00 - X + Z'],
        widget=widgets.RadioSelect())

    ctrlQ_B_earnings_err = models.CharField(
        choices=['13.00 + X', '13.00 - X', '13.00 - X - Z', '13.00 - X + Z'])


    #### SEARCH TASK FIELDS
    maxScreens = models.DecimalField(max_digits=5, decimal_places=2)
    screenTime = models.DecimalField(max_digits=5, decimal_places=2)
    pointDistMin = models.DecimalField(max_digits=5, decimal_places=2)
    pointDistMax = models.DecimalField(max_digits=5, decimal_places=2)

    task_reward = models.DecimalField(max_digits=5, decimal_places=2)
    target_income = models.DecimalField(max_digits=5, decimal_places=2)
    # add timestamps
    time_InitialStage1 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_GameInstructions = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_PracticeTask = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_SearchTask = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    # roles
    def role(self):
        if self.id_in_group == 1 and self.group.treatment != 'TP-R':
            return 'A'
        if self.id_in_group == 2 and self.group.treatment != 'TP-R':
            return 'B'
        if self.group.treatment == 'TP-R':
            return 'R'
    def searchRole(self):
        if self.id_in_group == 1:
            return 'A'
        if self.id_in_group == 2:
            return 'B'

    # gets the id of partner if you are matched, and of him/herself if the player is the reader
    def get_partner(self):
        if self.role() == 'A' or self.role() == 'B':
            return self.get_others_in_group()[0]
        elif self.role() == 'R':
            # OJO reader gets as partner him/herself!
            return self.group.get_player_by_role('R')


###################################


########################################################################################
# '''Draft zone'''

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
