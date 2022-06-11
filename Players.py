from city import *
from gaming_board import *
from attributes_boad import *
from Public_property import *


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

    def pay_rent_public(self, publicproperty: Publicproperties):
        self.cash_in_hand -= publicproperty.rent
        self.wealth -= publicproperty.rent

    def receive_rent_public(self, publicproperty: Publicproperties):
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

    def buy(self, city: City):
        pass

    def buy_property(self, city: City):
        self.cash_in_hand -= city.acquisition_cost
        self.properties.append(city)
        self.colours.append(city.colour)
        # self.wealth += price

    def buy_publicproperty(self, publicproperty: Publicproperties):
        self.cash_in_hand -= publicproperty.acquisition_cost
        self.publicproperty.append(publicproperty)
        publicproperty.totalproperty += 1
        # self.colours.append(pp.colour)

    def move_forward(self, num) -> LinkedList:
        curr = self.board
        for _ in range(num):
            curr = curr.next
            if isinstance(curr, Start):
                self.cash_in_hand += 200  # adds money when player passes through the start

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
