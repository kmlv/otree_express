from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class InitialCover(Page):
    """ Page 1: Cover Page """
    form_model = models.Player
    form_fields = ['time_InitialCover']
    # timeout_seconds = 60

page_sequence = [
    InitialCover
]
