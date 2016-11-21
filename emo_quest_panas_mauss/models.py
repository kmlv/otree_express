from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random

author = 'Kristian Lopez Vargas'

doc = """
This is a questionnaire for measuring emotions based on PANAS (___, 1988)
and a list of suggested emotions by Iris Mauss (UC Berkeley)
"""


class Constants(BaseConstants):
    name_in_url = 'emo_quest_panas_mauss'
    players_per_group = None
    num_rounds = 1

    emo_list = [
        'Accepted',
        'Active',
        'Afraid',
        'Alert',
        'Amused',
        'Angry',
        'Annoyed',
        'Anxious',
        'Ashamed',
        'Attentive',
        'Calm',
        'Contented (Peacefully Happy)',
        'Determined',
        'Distressed',
        'Down',
        'Embarrassed',
        'Energetic',
        'Enthusiastic',
        'Excited',
        'Gratitude',
        'Guilty',
        'Happy',
        'Hostile',
        'Inspired',
        'Interested',
        'Irritable',
        'Jittery',
        'Lonely',
        'Loving',
        'Negative (feel bad)',
        'Nervous',
        'Positive (feel good)',
        'Proud',
        'Rejected',
        'Sad',
        'Scared',
        'Strong',
        'Upset'
        ]

    # shuffle
    emo_list = random.sample(emo_list, len(emo_list))

    # list sizes
    emo_list_size = len(emo_list)
    num_emo_pg1 = int(round(emo_list_size / 2, 0))
    print('len1', num_emo_pg1)
    num_emo_pg2 = emo_list_size - num_emo_pg1
    print('len2',num_emo_pg2)


class Subsession(BaseSubsession):

    def before_session_starts(self):
        print(Constants.emo_list)

class Group(BaseGroup):
    pass

class Player(BasePlayer):

    time_emo_quest_pg1 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_emo_quest_pg2 = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_DoneQuestionnaire = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    # for i in range(len(Constants.emo_list)):
    #     temp = Constants.emo_list[i]
    #     locals()['{}'.format(temp)] = models.DecimalField(widget=widgets.HiddenInput(),
    #                                                       max_digits=3,
    #                                                       decimal_places=1,
    #                                                       min=1,
    #                                                       max=7
    #                                                       )

for var in Constants.emo_list:
    Player.add_to_class(
        '{}'.format(var),
        models.DecimalField(widget=widgets.HiddenInput(),
                            max_digits=3,
                            decimal_places=1,
                            min=1,
                            max=7
                            )
        )