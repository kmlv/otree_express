from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import random


class QuestionnairePage1(Page):

    form_fields = ['_'.join(Constants.emo_list_pg1[i]) for i in range(Constants.num_emo_pg1)]
    form_fields.append('time_emo_quest_pg1')
    form_model = models.Player

    def vars_for_template(self):
        # we shuffle emotion lists
        n1 = Constants.num_emo_pg1
        shuffled_emotion_list = random.sample(Constants.emo_list_pg1, n1)
        print("page1", shuffled_emotion_list)
        return {
            'emo_list_pg1': shuffled_emotion_list
        }


class QuestionnairePage2(Page):
    form_fields = ['_'.join(Constants.emo_list_pg2[i]) for i in range(Constants.num_emo_pg2)]
    form_fields.append('time_emo_quest_pg2')
    form_model = models.Player

    def vars_for_template(self):
        # we shuffle emotion lists
        # n1 = Constants.num_emo_pg1
        n2 = Constants.num_emo_pg2
        shuffled_emotion_list = random.sample(Constants.emo_list_pg2, n2)
        print("page2", shuffled_emotion_list)
        return {
            'emo_list_pg2': shuffled_emotion_list
        }



class DoneQuestionnaire(Page):
    form_model = models.Player
    form_fields = ['time_DoneQuestionnaire']
# pass
#    timeout_seconds = 10


page_sequence = [
    QuestionnairePage1,
    QuestionnairePage2,
    DoneQuestionnaire
]
