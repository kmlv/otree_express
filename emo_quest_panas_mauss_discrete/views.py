from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class EmoQuestPage1(Page):

    form_model = models.Player

    form_fields = ['panasmauss_{}'.format(var) for var in Constants.panasmauss_list[:Constants.num_emo_pg1]]
    form_fields.append('time_EmoQuestPage1')

    def vars_for_template(self):
        return {
            'emotions': Constants.panasmauss_list[:Constants.num_emo_pg1]
        }


class EmoQuestPage2(Page):

    form_model = models.Player

    form_fields = ['panasmauss_{}'.format(var) for var in Constants.panasmauss_list[Constants.num_emo_pg1:]]
    form_fields.append('time_EmoQuestPage2')

    def vars_for_template(self):
        return {
            'emotions': Constants.panasmauss_list[Constants.num_emo_pg1:]
        }


class DoneQuestionnaire(Page):
    pass


page_sequence = [
    EmoQuestPage1,
    EmoQuestPage2,
    DoneQuestionnaire
]
