from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Rachel Chen <me@rachelchen.me>'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'utility'
    players_per_group = None
    num_rounds = 1

    # Graph parameters
    mode = 'probability'    # valid options: 'single', 'independent', 'positive', 'negative', or 'probability'
    precision = 2           # number of decimcals
    scale = {
        'type': 'fixed',    # axis scaling, could be "fixed" or "dynamic"
        'max': 100          # only used in "fixed"
    }

    # labels
    label = {
        'x': 'x axis',
        'y': 'y axis'
    }

    # only used in probability mode
    constants = {
        'k': 0.4,          # scaling factor, only used in 'probability' mode
        'maxArea': 100
    }
    # only used in non-probability mode
    equation = {
        'm': 100,           # income
        'px': 1,            # price of X
        'py': 2,            # price of Y
        'a': {
            'x': 30,        # x value of point A
            'y': 80         # y value of point A
        },
        'b': {
            'x': 65,        # x value of point B
            'y': 45         # y value of point B
        }
    }

    width = 500             # width of the graph
    height = 500            # height of the graph
    margin = {              # grapg margins
        'top': 20,
        'right': 20,
        'bottom': 50,
        'left': 50
    }


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass
