from city import *
from gaming_board import *
from attributes_boad import *
from public_property import *
from Linked_list_api import *
from community_chest import *


class Players:
    """
    keeps track of the data of the players of the game.

    ===== PUBLIC ATTRIBUTES =====
    - cash_in_hand :
    - wealth :
    - properties :
    """

    def __init__(self):
        self.jail_num = 0
        self.cash_in_hand = 1500
        self.wealth = 1500
        link = player_set_up()
        self.board = link._first
        self.properties = []
        self.colours = []
        self.publicproperty = []

    def pay_rent(self, city: City):
        self.cash_in_hand -= city.rent
        self.wealth -= city.rent

    def receive_rent(self, city: City):
        self.cash_in_hand += city.rent
        self.wealth += city.rent

    def pay_rent_public(self, publicproperty: PublicProperties):
        self.cash_in_hand -= publicproperty.rent
        self.wealth -= publicproperty.rent

    def receive_rent_public(self, publicproperty: PublicProperties):
        if len(self.publicproperty) == 1:
            self.cash_in_hand += publicproperty.rent
            self.wealth += publicproperty.rent
        elif len(self.publicproperty) == 2:
            self.cash_in_hand += publicproperty.rent_with_two
            self.wealth += publicproperty.rent_with_two
        elif len(self.publicproperty) == 3:
            self.cash_in_hand += publicproperty.rent_with_three
            self.wealth += publicproperty.rent_with_three
        else:
            self.cash_in_hand += publicproperty.rent_with_four
            self.wealth += publicproperty.rent_with_four

    def update_rent(self, city: City) -> None:
        if self.colours.count(city.colour) == 3:
            verdict = input("want to buy house: ")
            if verdict == 'Y':
                self.cash_in_hand -= city.cost_of_house
                if city.number_of_houses == 0:
                    city.rent = city.rent_with_1_house
                    city.number_of_houses += 1
                elif city.number_of_houses == 1:
                    city.rent = city.rent_with_2_house
                    city.number_of_houses += 1
                elif city.number_of_houses == 2:
                    city.rent = city.rent_of_hotel
                    city.number_of_houses += 1

    def buy(self, city: City):
        pass

    def buy_property(self, city: City):
        self.cash_in_hand -= city.acquisition_cost
        self.properties.append(city)
        self.colours.append(city.colour)
        city.owner = True
        # self.wealth += price

    def buy_publicproperty(self, publicproperty: PublicProperties):
        self.cash_in_hand -= publicproperty.acquisition_cost
        self.publicproperty.append(publicproperty)
        publicproperty.totalproperty += 1
        publicproperty.owner = True
        # self.colours.append(pp.colour)

    def move_forward(self, num) -> LinkedList:
        curr = self.board
        for _ in range(num):
            curr = curr.next
            if isinstance(curr, Start):
                self.cash_in_hand += 200  # adds money when player passes through the start
                self.wealth += 200  # Wealth increases as well.

        self.board = curr
        return curr

    # def buy_property(self, property: City):
    #     self.properties.append(property)
    #     # todo
    #     self.wealth += property # buying cost from API of cities

    def send_to_jail(self):
        self.jail_num = 3

    def reduce_jail_sentence(self):
        self.jail_num -= 1
