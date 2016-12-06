from mock.mock import self
from otree.api import Currency as c, currency_range
#from otree.Models import subsession

from . import models
from ._builtin import Page, WaitPage
from .models import Constants

def vars_for_all_templates(self):
    return {'panasmauss_list': self.player.participant['panasmauss_list'],
            'panasmauss_list_1': self.player.participant['panasmauss_list_1'],
            'panasmauss_list_2': self.player.participant['panasmauss_list_2']
            }

class EmoQuestPage1(Page):

    form_model = models.Player

    form_fields = ['panasmauss_1{}'.format(var) for var in 'panasmauss_list_1']
    form_fields.append('time_EmoQuestPage1')

    def vars_for_template(self):
        return {
            'emotions': self.player.participant['panasmauss_list_1']
        }


class EmoQuestPage2(Page):

    form_model = models.Player
    form_fields = ['panasmauss_2{}'.format(var) for var in 'panasmauss_list_2']
    form_fields.append('time_EmoQuestPage2')

    def vars_for_template(self):
        return {
            'emotions': self.player.participant['panasmauss_list_2']
        }


class DoneQuestionnaire(Page):
    pass


page_sequence = [
    EmoQuestPage1,
    EmoQuestPage2,
    DoneQuestionnaire
]
