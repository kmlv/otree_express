from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Kristian Lopez Vargas'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'PTT_express_instructions'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    ####################################################################################################################
    # before session # this is a copy of Subsession in the PTT_expression models.py
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

    # this was a copy of Subsession in the PTT_expression models.py
    ####################################################################################################################


class Group(BaseGroup):
    # define vars
    treatment = models.TextField()
    value_type = models.TextField()
    elicitation_method = models.TextField()
    BDM_type = models.TextField()
    BDM_lolimit = models.TextField()
    BDM_uplimit = models.TextField()
    BDM_list_step = models.DecimalField(max_digits=5, decimal_places=2)

    # warning: falta timestamp


class Player(BasePlayer):
    # define vars
    endowment = models.CurrencyField()

    # warning: falta timestamp

    # this if for control questions

    ctrlQ_anonymity = models.CharField(
        verbose_name='Once you are paired with another participant, '
                     'will you ever know the identity of this other participant?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelectHorizontal())

    ctrlQ_who_transfers = models.CharField(
        verbose_name='Who decides how much to take from Role B’s account and deposit it into Role A’s account?',
        choices=['Role A', 'Role B', 'Role C', 'Role R', 'None of the above'],
        widget=widgets.RadioSelect())

    ctrlQ_B_always_sends = models.CharField(
        verbose_name='Will the participant in Role B always send a message to the participant in Role A '
                     'that he/she is matched with?',
        choices=['Yes', 'No', 'It depends on his/her valuation for sending a message'],
        widget=widgets.RadioSelect())

    ctrlQ_B_sends_message = models.CharField(
        verbose_name='Will the message written by Role B be sent in this case?',
        choices=['Yes', 'No'],
        widget=widgets.RadioSelectHorizontal())
    #labels are going to be defying directly in ControlQuestions.html file instead of verbose
    ctrlQ_A_earnings = models.CharField(
#        verbose_name='What are the final earnings for the participant in Role A? '
#                     '(Hints: endowment plus task income equals $13.00. Do not include participation fee)',
        choices=['13.00 + X', '13.00 - X', '13.00 - X - Z', '13.00 - X + Z'],
        widget=widgets.RadioSelect())

    ctrlQ_B_earnings = models.CharField(
#        verbose_name='What are the final earnings for the participant in Role B? '
#                    '(Hints: endowment plus task income equals $13.00. Do not include participation fee)',
        choices=['13.00 + X', '13.00 - X', '13.00 - X - Z', '13.00 - X + Z'],
        widget=widgets.RadioSelect())


    # roles
    def role(self):
        if self.id_in_group == 1 and self.group.treatment != 'TP-R':
            return 'A'
        if self.id_in_group == 2 and self.group.treatment != 'TP-R':
            return 'B'
        if self.group.treatment == 'TP-R':
            return 'R'




########################################################################################################################


# ctrlQ_B_sends_case2 = models.CharField(choices=['Yes', 'No'], widget=widgets.RadioSelectHorizontal(),
#                                        verbose_name='Will the message written by Role B be sent in this case?')
#
# ctrlQ_B_earnings_case2 = models.DecimalField(max_digits=5, decimal_places=2, min=0, max=100,
#                                              verbose_name='What are the final earnings for the participant in Role B? (do not include participation fee)')









# {#    In order to assure that everyone understands the rules of today’s experiment, we ask you to answer the
# following questions. Please raise your hand once you are done and an experimenter will attend to you.#}
# {#    1. Once you are paired with another participant, will you ever know the identity of this other participant?  #}
# {#    Answer: Yes   No#}
# {#    2. If you are assigned the role B, will you decide how much to transfer into A’s account?#}
# {#    Answer: Yes . No .#}
# {#    3.  If you are assigned the role of B, will you be able to send a written message to your counterpart A, for sure?  #}
# {#    Answer: Yes . No .#}
#
#     5.  Suppose John and his counterpart each earned $10.00 of task income. Later, John is assigned Role B.
# Then, his counterpart A transfers an $X amount from John’s account into A’s account.  John (B) submits $2.00 as his
# willingness to pay to send a message to A. Please, answer the following questions using this information.#}
# {#    (a)        If the actual price randomly drawn by the computer is $1.00, what are the total earnings for
# the participant with role A and B? #}
# {##}
# {#    Answer for A’s earnings (in $)#}
# {#    10 - X #}
# {#    10 + X#}
# {#    10#}
# {##}
# {#    Answers for B’s earnings (in $)#}
# {#    10 - X - 1#}
# {#    10 - X - 2#}
# {#    10 - X#}
# {##}
# {##}
# {#    (b)   	If the actual price randomly drawn by the computer is $3.00, what are the total earnings for the
# participant with role A and B? #}
# {##}
# {##}
# {#    Answer for A’s earnings (in $)#}
# {#    10 - X #}
# {#    10 + X#}
# {#    10#}
# {##}
# {##}
# {#    Answers for B’s earnings (in $)#}
# {#    10 - X - 2#}
# {#    10 - X - 3#}
# {#    10 - X#}
