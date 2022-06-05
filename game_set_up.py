from chance import *
from Players import *
from random import randint, seed
from Linked_list_api import *
from attributes_boad import *
from city import *


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
            # seed(10)
            # print(dice)

            current_tile = player.move_forward(dice).item

            if isinstance(current_tile, City):

                if not current_tile.owner and current_tile not in player.properties:  # what if the owner is the person itself? # also check if there is an owner
                    player.pay_rent(current_tile)
                    player_recieve = who_property(list_players, current_tile)
                    player_recieve.receive_rent(current_tile)
                    # Idk why is this a problem -> since type contact is city
                    # and this not city but its sub class

                elif player.cash_in_hand >= current_tile.acquisition_cost:
                    verdict = input(F"Do you want to buy the property for{current_tile.acquisition_cost}?(Y/N)")
                    if verdict == 'Y':
                        player.buy_property(current_tile)

                    # ask for the options of what to do
                    print("yp")
                # else the player has insufficient fund -> no options by py qt

            elif isinstance(current_tile, Jail):  # stuck for 3 rounds or pay certain amount to get out
                verdict = input("stuck for 3 rounds or pay 150 to get out: ")  # py qt button
                jail_decision(player, verdict)

            elif isinstance(current_tile, Chance):
                pass
            elif isinstance(current_tile, Start):
                player.cash_in_hand += 200
                player.wealth += 200
                # if the tile is Start do nothing as +200
                # is handled in player api

        # check the status of this player
        # if bankrupt, ie, if money is less than $-500
        if player.cash_in_hand < -500:
            # python qt line === you are bankrupt ===
            list_players.delete_player(player)
        if len(list_players) == 1:
            # python qt line === you won ===
            break
        if player.cash_in_hand > 3000:
            # python qt line === you won ===
            break
        curr = curr.next  # gets the next player


def jail_decision(player: Players, decision: str) -> None:
    if decision == "pay":
        player.cash_in_hand -= 150  # player pays $150 to get out, need to check whether wealth decreases too
    else:
        player.send_to_jail()


'''def buy_or_not(player: Players, decision: str) -> None:
    if decision == 'Y':
        player.buy_property()'''


def who_property(list_players: LinkedList, city: City) -> Players:
    """
    list_players: LinkedList of players
    city: A property
    :return: Returns the player who has the property.
    """
    curr = list_players._first
    while curr is not None:
        player = curr.item
        if city in player.properties:
            return player
        curr = curr.next


game_formation()
