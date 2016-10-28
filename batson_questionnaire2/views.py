from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class QuestionnairePage1(Page):

    form_fields = ['_'.join(Constants.emotion_list[i]) for i in range(len(Constants.emotion_list))]
    form_fields.append('time_batson1')
    form_model = models.Player

    def vars_for_template(self):
        # we shuffle emotion lists
        shuffled_emotion_list = random.sample(Constants.emotion_list, len(Constants.emotion_list))
        print(shuffled_emotion_list)
        return {
            'emo_list': shuffled_emotion_list
        }

    timeout_seconds = 600


class QuestionnairePage2(Page):

    form_fields = ['_'.join(Constants.filler_list[i]) for i in range(len(Constants.filler_list))]
    form_fields.append('time_batson2')
    form_model = models.Player


    def vars_for_template(self):
        # we shuffle filler lists
        shuffled_filler_list = random.sample(Constants.filler_list, len(Constants.filler_list))
        print(shuffled_filler_list)
        return {
            'filler_list': shuffled_filler_list
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass

    timeout_seconds = 600


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
