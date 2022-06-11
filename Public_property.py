class Publicproperties:
    """
    These are properties such as Railways, Airport etc
    according to Plato
    """

    def __init__(self):
        self.owner = False
        self.acquisition_cost = 0
        self.rent = 35
        self.sell_price = 0
        self.rent_with_two = 70
        self.rent_with_three = 105
        self.rent_with_four = 140
        self.totalproperty=0

    def is_owner(self):
        return self.owner


class Harbour(Publicproperties):
    def __init__(self):
        super().__init__()
        # self.owner = False
        self.acquisition_cost = 100
        # self.rent = 35
        self.sell_price = 80


class Railway(Publicproperties):
    def __init__(self):
        super().__init__()
        # self.owner = False
        self.acquisition_cost = 150
        # self.rent = 35
        self.sell_price = 120


class Electricity(Publicproperties):
    def __init__(self):
        super().__init__()
        # self.owner = False
        self.acquisition_cost = 200
        # self.rent = 35
        self.sell_price = 160


class Airport(Publicproperties):
    def __init__(self):
        super().__init__()
        # self.owner = False
        self.acquisition_cost = 250
        # self.rent = 35
        self.sell_price = 200
