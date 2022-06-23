from Linked_list_api import *
from city import *
from attributes_boad import *
from community_chest import *
from public_property import *
from auction import *

Start = Start()
Delhi = Delhi()
Tokyo = Tokyo()
Paris = Paris()
Railway = Railway()
London = London()
Oslo = Oslo()
#CommunityChest = CommunityChest()
Toronto = Toronto()
Harbour = Harbour()
LosAngeles = LosAngeles()
Waterloo = Waterloo()
Jail = Jail()
Sydney = Sydney()
Seoul = Seoul()
Bangkok = Bangkok()
Electricity = Electricity()
Shanghai = Shanghai()
Moscow = Moscow()
Auction = Auction()
Cairo = Cairo()
Airport = Airport()
Madrid = Madrid()
Jakarta = Jakarta()
Peru = Peru()

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
