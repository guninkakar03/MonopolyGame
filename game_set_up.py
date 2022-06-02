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
        # add a condition for bankuptacy
        player = curr.item
        if player.jail_num > 0: # checks if the player is in jail or not
            player.reduce_jail_sentence()
        else:
            dice = randint(1, 6)
            # seed(10)
            # print(dice)

            current_tile = player.move_forward(dice).item

            if issubclass(current_tile, City):
                if current_tile.owner :  # what if the owner is the person itself? # also check if there a owner

                    player.pay_rent(111) # write code to get rent value
                else:
                    # ask for the options of what to do
                    print("yp")
                    player.buy(current_tile)
            elif isinstance(current_tile, Jail): # stuck for 3 rounds or pay certain amount to get out
                verdict = input("stuck for 3 rounds or pay 150 to get out: ") # py qt button
                jail_decision(player, verdict)

            elif isinstance(current_tile, Chance):
                pass
            elif isinstance(current_tile, Start): # if the tile is
                pass
        # check the status of this player
        # if bankrupt, ie, if money is less than $-500
        #
        curr = curr.next  # gets the next player
        break


def jail_decision(player: Players, decision: str) -> None:
    if decision == "pay":
        player.pay_rent(150) # player pays $150 to get out
    else:
        player.send_to_jail()

game_formation()

