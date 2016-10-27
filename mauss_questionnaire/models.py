from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


author = 'Kristian Lopez Vargas'

doc = """
This is a questionnaire for measuring emotions based on a list of suggested emotions
by Iris Mauss (UC Berkeley)
"""


class Constants(BaseConstants):
    name_in_url = 'mauss_questionnaire'
    players_per_group = None
    num_rounds = 1

    mauss_list = [
        'Accepted',
        'Amused',
        'Angry',
        'Annoyed',
        'Anxious',
        'Calm',
        'Contented (Peacefully Happy)',
        'Distressed',
        'Down',
        'Embarrassed',
        'Energetic',
        'Excited',
        'Gratitude',
        'Happy',
        'Interested',
        'Lonely',
        'Loving',
        'Negative (feel bad)',
        'Nervous',
        'Positive (feel good)',
        'Rejected',
        'Sad'
    ]

    # shuffle
    mauss_list = random.sample(mauss_list, len(mauss_list))

    num_emo_pg1 = int(round(len(mauss_list)/2, 0))
    num_emo_pg2 = len(mauss_list) - num_emo_pg1


class Subsession(BaseSubsession):

    def before_session_starts(self):
        print(Constants.mauss_list)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    time_mauss1 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_mauss2 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    for i in range(len(Constants.mauss_list)):
        temp = Constants.mauss_list[i]
        locals()['{}'.format(temp)] = models.DecimalField(widget=widgets.HiddenInput(),
                                                          max_digits=3,
                                                          decimal_places=1,
                                                          min=1,
                                                          max=9
                                                          )
