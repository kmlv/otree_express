from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'zzz_test_app'
    players_per_group = None
    num_groups = 3
    num_rounds = 1
    endowment = c(100)
    efficiency_factor = 1.8


class Subsession(BaseSubsession):
    pass
    #def before_session_starts(self):
     #   new_structure = [[1], [2], [3]]
      #  self.set_group_matrix(new_structure)
class Group(BaseGroup):
    total_contribution = models.CurrencyField()
    individual_share = models.CurrencyField()

    def set_payoffs(self):
        self.total_contribution = sum(
            [p.contribution for p in self.get_group_matrix()])
        self.individual_share = self.total_contribution * Constants.efficiency_factor / 2
        for p in self.get_group_matrix():
            p.payoff = Constants.endowment - p.contribution + self.individual_share


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)
    def get_partner(self):
        return self.get_others_in_subsession()[0]



    # roles
    # def role(self):
    #     i = 0
    #     for grupo in self.group
    #     return self.