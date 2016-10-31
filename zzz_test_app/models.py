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
    players_per_group = 2
    num_groups = 2
    num_rounds = 1
    endowment = c(100)
    efficiency_factor = 1.8


class Subsession(BaseSubsession):
    pass
    #def get_partner(self):
     #       return self.get_others_in_subsession()[0]
     #  new_structure = [[1], [2], [3]]
      # self.set_group_matrix(new_structure)

class Group(BaseGroup):
    total_contribution1 = models.CurrencyField()
    total_contribution2 = models.CurrencyField()
    individual_share1 = models.CurrencyField()
    individual_share2 = models.CurrencyField()

    def set_payoffs(self):

        self.total_contribution1 = sum(
            [p.contribution for p in self.get_player_by_role('A')])
        self.total_contribution2 = sum(
            [p.contribution for p in self.get_player_by_role('B')])
        self.individual_share1 = self.total_contribution1 * Constants.efficiency_factor / 2
        self.individual_share2 = self.total_contribution2 * Constants.efficiency_factor / 2
        for p in self.get_player_by_role('A'):
            p.payoff = Constants.endowment - p.contribution + self.individual_share1
        for p in self.get_player_by_role('B'):
            p.payoff = Constants.endowment - p.contribution + self.individual_share2


class Player(BasePlayer):
    contribution = models.CurrencyField(min=0, max=Constants.endowment)
    def role(self):
        if self.id_in_group == 1:
            return 'A'
        elif self.id_in_group == 2:
            return 'B'
    def get_partner(self):
        return self.get_others_in_subsession()[0]



    # roles
    # def role(self):
    #     i = 0
    #     for grupo in self.group
    #     return self.