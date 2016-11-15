from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'PANAS_final'
    players_per_group = None
    num_rounds = 1
    panas_list = [
        'Interested',
        'Distressed',
        'Excited',
        'Upset',
        'Strong',
        'Guilty',
        'Scared',
        'Hostile',
        'Enthusiastic',
        'Proud',
        'Irritable',
        'Alert',
        'Ashamed',
        'Inspired',
        'Nervous',
        'Determined',
        'Attentive',
        'Jittery',
        'Active',
        'Afraid'
    ]


class Subsession(BaseSubsession):

    def before_session_starts(self):
        pass
        # print(Constants.emotion_list)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    time_panas1 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_panas2 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

#

for var in Constants.panas_list:
    Player.add_to_class(
        'panas_{}'.format(var),
        models.IntegerField(
            initial=None,
            choices=[
                [1, 'Not at all  '],
                [2, 'A Little  '],
                [3, 'Moderately  '],
                [4, 'Quite a bit  '],
                [5, 'Extremely  ']
                ],
            verbose_name=var,
            widget=widgets.RadioSelectHorizontal()
        )
        )


# for emotion in range(10):
#     Group.add_to_class(
#         'cash_{}'.format(amount),
#         models.BooleanField(
#             widget=widgets.RadioSelectHorizontal(),
#             choices=[[True, ''], [False, '']],
#             verbose_name='{}'.format(c(amount))
#         )
#     )

###################
# DRAFT

# for i in range(len(Constants.emotion_list)):
#     temp = '_'.join(Constants.emotion_list[i])
#     print(temp)
#     Player.add_to_class(
#         '{}'.format(temp),
#         models.DecimalField(max_digits=5, decimal_places=2, min=0, max=10)
#     )
