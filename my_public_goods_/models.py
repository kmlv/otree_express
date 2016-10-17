from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range, safe_json
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_public_goods_'
    players_per_group = 3
    num_rounds = 1

    endowment = c(100)
    efficiency_factor = 1.8


class Player(BasePlayer):

    contribution = models.CurrencyField(min=0, max=Constants.endowment)


class Group(BaseGroup):

    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / Constants.players_per_group
        for p in self.get_players():
            p.payoff = Constants.endowment - p.contribution + self.individual_share


class Subsession(BaseSubsession):
    pass
