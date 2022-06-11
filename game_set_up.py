from chance import *
from players import *
from random import randint, seed
from Linked_list_api import *
from attributes_boad import *
from city import *
from public_property import *


def game_formation() -> None:
    player1 = Players()
    player2 = Players()
    player3 = Players()
    player4 = Players()

    list_players = LinkedList([player1, player2, player3, player4])
    curr = list_players._first

    while True:
        # add a condition for bankruptcy
        player = curr.item
        if player.jail_num > 0:  # checks if the player is in jail or not
            player.reduce_jail_sentence()
        else:
            dice = randint(1, 6)
            current_tile = player.move_forward(dice).item
            if dice == 6:
                new_dice = randint(1, 6)
                current_tile = player.move_forward(new_dice).item

            if isinstance(current_tile, City):
                property_decision(current_tile, player, list_players)
                player.update_rent(current_tile)

            elif isinstance(current_tile, Jail):  # stuck for 3 rounds or pay certain amount to get out
                verdict = input("stuck for 3 rounds or pay 150 to get out: ")  # py qt button
                jail_decision(player, verdict)

            elif isinstance(current_tile, CommunityChest):
                pass
            elif isinstance(current_tile, Start):
                pass
                # i removed the 200 thing as it is already covered in
                # player.move_forward - check it out ;)

            elif isinstance(current_tile, Publicproperties):
                public_property_decision(current_tile, player, list_players)

        # check the status of this player
        # if bankrupt, ie, if money is less than $-500
        if player.cash_in_hand < -500:
            # python qt line === you are bankrupt ===
            list_players.delete_player(player)  # I believe this would be a problem - let's discuss asap!
        if len(list_players) == 1:
            # python qt line === you won ===
            break
        if player.cash_in_hand >= 3000:
            # python qt line === you won ===
            break
        curr = curr.next  # gets the next player


def property_decision(current_tile: City, player: Players, list_players: LinkedList) -> None:
    # checks if the property is owned
    if current_tile.owner and current_tile not in player.properties:

        player.pay_rent(current_tile)
        player_receive = who_property(list_players, current_tile)
        player_receive.receive_rent(current_tile)

    elif player.cash_in_hand >= current_tile.acquisition_cost:
        verdict = input(F"Do you want to buy the property for{current_tile.acquisition_cost}?(Y/N)")
        if verdict == 'Y':
            player.buy_property(current_tile)  # check this
    else:
        pass
        # py qt ===insufficient funds===


def public_property_decision(current_tile: Publicproperties, player: Players, list_players: LinkedList) -> None:
    if not current_tile.owner and current_tile not in player.publicproperty:
        # player.pay_rent(current_tile)
        player_receive = who_public_property(list_players, current_tile)
        if len(player_receive.publicproperty) == 1:
            player.pay_rent_public(current_tile)
        elif len(player_receive.publicproperty) == 2:
            player.cash_in_hand -= current_tile.rent_with_two
            player.wealth -= current_tile.rent_with_two
        elif len(player_receive.publicproperty) == 3:
            player.cash_in_hand -= current_tile.rent_with_three
            player.wealth -= current_tile.rent_with_three
        else:
            player.cash_in_hand -= current_tile.rent_with_four
            player.wealth -= current_tile.rent_with_four
        player_receive.receive_rent_public(current_tile)

    elif player.cash_in_hand >= current_tile.acquisition_cost:
        verdict = input(F"Do you want to buy the property for{current_tile.acquisition_cost}?(Y/N)")
        if verdict == 'Y':
            player.buy_publicproperty(current_tile)  # check this
    else:
        pass


def who_property(list_players: LinkedList, city: City) -> Players:
    """
    list_players: LinkedList of players
    city: A property
    :return: Returns the player who has the property.
    """
    curr = list_players._first
    while curr.next is not list_players._first:
        player = curr.item
        if city in player.properties:
            return player
        curr = curr.next


def who_public_property(list_players: LinkedList, public_property: Publicproperties) -> Players:
    """
    list_players: LinkedList of players
    public_property: A property
    :return: Returns the player who has the property.
    """
    curr = list_players._first
    while curr.next is not list_players._first:
        player = curr.item
        if public_property in player.publicproperty:
            return player
        curr = curr.next


def jail_decision(player: Players, decision: str) -> None:
    if decision == "pay":
        player.cash_in_hand -= 150  # player pays $150 to get out, need to check whether wealth decreases too
    else:
        player.send_to_jail()


'''def buy_or_not(player: Players, decision: str) -> None:
    if decision == 'Y':
        player.buy_property()'''

game_formation()
