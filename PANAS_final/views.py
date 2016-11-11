from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class QuestionnairePage1(Page):

    form_model = models.Player

    form_fields = ['panas_{}'.format(var) for var in Constants.panas_list[:10]]
    form_fields.append('time_panas1')

    def vars_for_template(self):
        return {
            'emotions': Constants.panas_list[:10]
        }


class QuestionnairePage2(Page):

    form_model = models.Player

    form_fields = ['panas_{}'.format(var) for var in Constants.panas_list[10:]]
    form_fields.append('time_panas2')

    def vars_for_template(self):
        return {
            'emotions': Constants.panas_list[10:]
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class DoneQuestionnaire(Page):

    timeout_seconds = 10


page_sequence = [
    QuestionnairePage1,
    QuestionnairePage2,
    DoneQuestionnaire
]

#########################################
# Draft zoe

# if you want to make it random within the pair of moods
# for i in range(len(Constants.emotion_list)):
#     shuffled_emotion_list[i] = random.sample(shuffled_emotion_list[i], len(Constants.emotion_list[i]))

# using a get_form_fields function
# def get_form_fields(self):
# form_fields = []
# for i in range(len(Constants.emotion_list)):
#     var = '_'.join(Constants.emotion_list[i])
#     form_fields.append(var)
# return ['_'.join(Constants.emotion_list[i]) for i in range(len(Constants.emotion_list))]
