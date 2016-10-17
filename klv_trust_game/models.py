from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Kristian Lopez Vargas'

doc = """
This is my learning version of the trust game
"""

class Constants(BaseConstants):
    name_in_url = 'klv_trust_game'
    players_per_group = 2
    num_rounds = 1

    endowment = c(10)
    multiplication_factor = 3

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):

    sent_amount = models.CurrencyField(
        choices=currency_range(0, Constants.endowment, c(1)),
    )
    sent_back_amount = models.CurrencyField()

    tripled_amount = models.CurrencyField()

    def set_payoffs(self):
        p1 = self.get_player_by_id(1)
        p2 = self.get_player_by_id(2)
        p1.payoff = Constants.endowment - self.sent_amount + self.sent_back_amount
        p2.payoff = self.sent_amount * Constants.multiplication_factor - self.sent_back_amount


class Player(BasePlayer):
    pass
