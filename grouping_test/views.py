from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage1(Page):
    pass


class MyPage2(Page):
    pass


class WaitForGroup2(WaitPage):
    wait_for_all_groups = True

    def is_displayed(self):
        return self.player.id_in_group == 1


page_sequence = [
    MyPage1,
    WaitForGroup2,
    MyPage2
]
