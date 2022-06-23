# #from players import Players
# from Linked_list_api import *
# from players import *
# from gaming_board import *
# from random import randint
# from city import *
# from attributes_boad import *
#
#
# class CommunityChest:
#     def perform(self, player: Players, list_players: LinkedList):
#         raise NotImplementedError
#
#
# class Task1(CommunityChest):
#     """
#     pay everyone $25
#     """
#
#     def perform(self, player: Players, list_players: LinkedList):
#         player.cash_in_hand -= 100
#         curr = list_players._first
#         while curr.next is not list_players._first:
#             player_rem = curr.item
#             if not player_rem == player:
#                 player_rem.cash_in_hand += 25
#             curr = curr.next
#
#
# class Task2(CommunityChest):
#     """
#     everyone pays the player $25
#     """
#
#     def perform(self, player: Players, list_players: LinkedList):
#         player.cash_in_hand += 100
#         curr = list_players._first
#         while curr.next is not list_players._first:
#             player_rem = curr.item
#             if not player_rem == player:
#                 player_rem.cash_in_hand -= 25
#             curr = curr.next
#
#
# class Task3(CommunityChest):
#     """
#     Go to jail
#     """
#
#     def perform(self, player: Players, list_players: LinkedList):
#         player.send_to_jail()
#
#
# class Task4(CommunityChest):
#     """
#     go to a random place
#     - chooses a random place on the map
#     """
#
#     def perform(self):
#         pass
#
#
# class Task5(CommunityChest):
#     """
#     go back 3 spaces
#     """
#
#     def perform(self):
#         pass
#
#
# class Task6(CommunityChest):
#     """
#     go forward 3 spaces
#     """
#
#     def perform(self, player: Players) -> None:
#         player.move_forward(3)
#
#
# class Task7(CommunityChest):
#     """
#     pay income tax - 20% of property's rent
#     """
#
#     def perform(self, player: Players) -> None:
#         rent_total = 0
#         for property in player.properties:
#             rent_total = +property.rent
#         player.cash_in_hand -= rent_total
#         player.wealth -= rent_total
