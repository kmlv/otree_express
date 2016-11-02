from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""
#my message to chris
        #For example, in the public game with 2 players and 2 groups,
        # I want that the P1 plays with P3 (from first and second group respectively ),
        #  and the same with P2 and P4.
        #  I tried to assign the role of 'A' to P1 and P3, and the role  'B' to P2 and P4
#chris recomendation
        #That's fine, you can shuffle the groups at any time using set_group_matrix, group_randomly, etc.
        #  The groups don't have to always be the same.
        # Or you can put all players in 1 group, and then get all A players with:
        # [p for p in self.get_players() if p.role() == 'A']
class Constants(BaseConstants):
    name_in_url = 'grouping_test'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
