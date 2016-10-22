from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random

class MyPage(Page):

    # def get_form_fields(self):
        # form_fields = []
        # for i in range(len(Constants.emotion_list)):
        #     var = '_'.join(Constants.emotion_list[i])
        #     form_fields.append(var)
        # return ['_'.join(Constants.emotion_list[i]) for i in range(len(Constants.emotion_list))]

    form_fields = ['_'.join(Constants.emotion_list[i]) for i in range(len(Constants.emotion_list))]
    form_model = models.Player

    def vars_for_template(self):
        # we shuffle emotion lists
        shuffled_emotion_list = random.sample(Constants.emotion_list, len(Constants.emotion_list))
        print(shuffled_emotion_list)
        return {
            'emo_list': shuffled_emotion_list
        }


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class DoneQuestionnaire(Page):
    pass


class Results(Page):
    pass


page_sequence = [
    MyPage,
    DoneQuestionnaire
]
