class CommunityChest:
    def perform(self):
        raise NotImplementedError


class Task1(CommunityChest):
    """
    pay everyone $25
    """
    pass

    def perform(self):
        pass


class Task2(CommunityChest):
    """
    everyone pays the player $25
    """
    pass

    def perform(self):
        pass


class Task3(CommunityChest):
    """
    Go to jail
    """
    pass

    def perform(self):
        pass


class Task4(CommunityChest):
    """
    go to a random place
    - chooses a random place on the map
    """
    pass

    def perform(self):
        pass


class Task5(CommunityChest):
    """
    go back 3 spaces
    """
    pass

    def perform(self):
        pass


class Task6(CommunityChest):
    """
    go forward 3 spaces
    """
    pass

    def perform(self):
        pass


class Task7(CommunityChest):
    """
    pay income tax - 20% of property's rent
    """
    pass

    def perform(self):
        pass
