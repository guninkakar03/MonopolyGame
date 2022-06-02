from Linked_list_api import *
from city import *
from attributes_boad import *
Gaming_board = [Start,
                Delhi,
                Tokyo,
                Paris,
                London,
                LosAngeles,
                Oslo,
                Toronto,
                Mumbai,
                Wuhan,
                Moscow,
                Cairo,
                Seoul,
                Shanghai,
                Brazil,
                Bangkok,
                Sydney,
                Peru,
                Istanbul,
                Dhaka,
                Jakarta,
                Madrid,
                Waterloo]


def player_set_up() -> LinkedList:

    linky = LinkedList(Gaming_board)
    return linky
