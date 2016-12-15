from django import template

register = template.Library()


@register.filter
def index(sequence, position):
    return sequence[position]


@register.filter
def allButLast(sequence):
    temp = list(sequence)
    return temp[:-1]