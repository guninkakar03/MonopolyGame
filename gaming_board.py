from Linked_list_api import *
from city import *
from attributes_boad import *
from community_chest import *
from Public_property import *
from auction import *

Gaming_board = [Start,
                Delhi,
                Tokyo,
                Paris,
                Railway,
                London,
                Oslo,
                CommunityChest,
                Toronto,
                Harbour,
                Mumbai,
                LosAngeles,
                Waterloo,
                Jail,
                Sydney,
                Seoul,
                Bangkok,
                Electricity,
                Shanghai,
                Moscow,
                Auction,
                Cairo,
                Airport,
                Madrid,
                Jakarta,
                Peru]


def player_set_up() -> LinkedList:
    linky = LinkedList(Gaming_board)
    return linky
