from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'batson_questionnaire'
    players_per_group = None
    num_rounds = 1
    emotion_list = [
        ['em11', 'em12'],
        ['em21', 'em22'],
        ['em31', 'em32'],
    ]

class Subsession(BaseSubsession):

    def before_session_starts(self):
        print(Constants.emotion_list)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # for i in range(len(Constants.emotion_list)):
    #     temp = '_'.join(Constants.emotion_list[i])
    #     print(temp)
    #     Player.add_to_class(
    #         '{}'.format(temp),
    #         models.DecimalField(max_digits=5, decimal_places=2, min=0, max=10)
    #     )

    for i in range(len(Constants.emotion_list)):
        temp = '_'.join(Constants.emotion_list[i])
        locals()['{}'.format(temp)] = models.DecimalField(max_digits=5, decimal_places=2, min=0, max=10)