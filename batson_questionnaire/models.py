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
        ['Bad mood', 'Good mood'],
        ['Sad', 'Happy'],
        ['Depressed', 'Elated'],
        ['Dissatisfied', 'Satisfied'],
        ['Gloomy', 'Cheerful'],
        ['Displeased', 'Pleased'],
        ['Sorrowful', 'Joyful']
    ]

    filler_list = [
        ['Nervous', 'Calm'],
        ['Tense', 'Relaxed'],
        ['Uncomfortable', 'Comfortable'],
        ['Apathetic', 'Caring'],
        ['Lethargic', 'Energetic'],
        ['Unconfident', 'Confident'],
        ['Unresponsive', 'Emotional'],
        ['Passive', 'Active']
    ]


class Subsession(BaseSubsession):

    def before_session_starts(self):
        print(Constants.emotion_list)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    for i in range(len(Constants.emotion_list)):
        temp = '_'.join(Constants.emotion_list[i])
        locals()['{}'.format(temp)] = models.DecimalField(widget=widgets.HiddenInput(),
                                                          max_digits=3,
                                                          decimal_places=1,
                                                          min=1,
                                                          max=9
                                                          )

    for i in range(len(Constants.filler_list)):
        temp = '_'.join(Constants.filler_list[i])
        locals()['{}'.format(temp)] = models.DecimalField(widget=widgets.HiddenInput(),
                                                          max_digits=3,
                                                          decimal_places=1,
                                                          min=1,
                                                          max=9
                                                          )



###################
# DRAFT

# for i in range(len(Constants.emotion_list)):
#     temp = '_'.join(Constants.emotion_list[i])
#     print(temp)
#     Player.add_to_class(
#         '{}'.format(temp),
#         models.DecimalField(max_digits=5, decimal_places=2, min=0, max=10)
#     )
