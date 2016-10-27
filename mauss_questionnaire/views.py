from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class QuestionnairePage1(Page):

    form_fields = [Constants.mauss_list[i] for i in range(0, Constants.num_emo_pg1)]
    form_fields.append('time_mauss1')
    form_model = models.Player

    def vars_for_template(self):
        # we shuffle emotion lists
        n1 = Constants.num_emo_pg1
        shuffled_emotion_list = random.sample(Constants.mauss_list[:n1], n1)
        print(shuffled_emotion_list)
        return {
            'emo_list': shuffled_emotion_list
        }


class QuestionnairePage2(Page):
    form_fields = [Constants.mauss_list[i] for i in range(Constants.num_emo_pg1, Constants.num_emo_pg2)]
    form_fields.append('time_mauss2')
    form_model = models.Player


    def vars_for_template(self):
        # we shuffle emotion lists
        n1 = Constants.num_emo_pg1
        n2 = Constants.num_emo_pg2
        shuffled_emotion_list = random.sample(Constants.mauss_list[n1:n1+n2], n2)
        print(shuffled_emotion_list)
        return {
            'emo_list': shuffled_emotion_list
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
