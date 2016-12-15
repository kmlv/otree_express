from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from    .models import Constants


class EmoQuestPage1(Page):

    form_model = models.Player

    def get_form_fields(self):
        li = ['panasmauss_{}'.format(var) for var in self.session.vars['panasmauss_list_1']]
        li.append('time_EmoQuestPage1')
        return li

    def vars_for_template(self):
        return {
            'emotions': self.session.vars['panasmauss_list_1']
        }


class EmoQuestPage2(Page):

    form_model = models.Player

    def get_form_fields(self):
        li = ['panasmauss_{}'.format(var) for var in self.session.vars['panasmauss_list_2']]
        li.append('time_EmoQuestPage2')
        return li

    def vars_for_template(self):
        return {
            'emotions': self.session.vars['panasmauss_list_2']
        }

class DoneQuestionnaire(Page):
    pass


page_sequence = [
    EmoQuestPage1,
    EmoQuestPage2,
    DoneQuestionnaire
]
