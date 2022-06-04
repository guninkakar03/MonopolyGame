class City:
    """
    NOTE: can make a house only if there are 3 same coloured block owned by
    a player.

    """
    rent: int
    owner: bool
    acquisition_cost: int

    def __init__(self):
        self.owner = False
        self.acquisition_cost = 0
        self.rent = 0
        self.cost_of_house = 100
        self.cost_of_hotel = 100
        self.number_of_houses = 10
        self.rent_with_1_house = 0
        self.rent_with_2_house = 0
        self.rent_of_hotel = 10
        self.colour = ""

    def is_owner(self):
        return self.owner


# ==============================================================================
# cities of red tile
# ==============================================================================
class Delhi(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 17
        self.number_of_houses = 0
        self.rent_with_1_house = 100
        self.rent_with_2_house = 234
        self.rent_of_hotel = 365
        self.colour = "red"


class Tokyo(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "red"


class Paris(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 35
        self.number_of_houses = 0
        self.rent_with_1_house = 175
        self.rent_with_2_house = 310
        self.rent_of_hotel = 410
        self.colour = "red"


# ==============================================================================
# cities of blue tile
# ==============================================================================


class London(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"

# todo

class Oslo(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"


class Toronto(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



# ==============================================================================
# cities of black tile
# ==============================================================================


class Mumbai(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class LosAngeles(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Waterloo(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



# ==============================================================================
# cities of brown tile
# ==============================================================================


class Shanghai(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Moscow(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Cairo(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



# ==============================================================================
# cities of yellow tile
# ==============================================================================
class Sydney(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Seoul(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Bangkok(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



# ==============================================================================
# cities of green tile
# ==============================================================================

class Madrid(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Jakarta(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"



class Peru(City):
    def __init__(self):
        City.__init__(cost_of_house, cost_of_hotel)
        self.owner = False
        self.acquisition_cost = 100
        self.rent = 27
        self.number_of_houses = 0
        self.rent_with_1_house = 110
        self.rent_with_2_house = 220
        self.rent_of_hotel = 350
        self.colour = "blue"


class Brazil(City):
    pass


class Istanbul(City):
    pass


class Dhaka(City):
    pass


class Wuhan(City):
    pass
