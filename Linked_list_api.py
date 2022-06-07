from __future__ import annotations
from typing import Any, Optional

"""
Rules of the Monopoly Game:

1. Every player gets $1500 as starting amount

2. Every country can be bought by the player if they land on it indicated 
by the dice

3. If another player passes through an already bought property, 
then they pay a certain rent.
(Should be done automatically by the data stored in the classes) 

4. The game can be won if the net worth exceeds a certain amount 
(cash in hand + property wealth)

5. If the player owns debt over a certain amount,they will be declared bankrupt.

"""


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The _first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    # def __init__(self) -> None:
    #     """Initialize a new empty linked list containing the given items.
    #     """
    #     self._first = None

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The _first node in the linked list contains the _first item
        in <items>.
        """
        self._first = None
        node = None
        curr_node = None
        for item in items:
            if node is None:
                new_node = _Node(item)
                node = new_node
                curr_node = node
            else:
                new_node = _Node(item)
                curr_node.next = new_node
                curr_node = new_node
        self._first = node
        curr_node.next = self._first

    # ------------------------------------------------------------------------
    # Methods from lecture/readings
    # ------------------------------------------------------------------------
    def is_empty(self) -> bool:
        """Return whether this linked list is empty.

        >>> LinkedList([]).is_empty()
        True
        >>> LinkedList([1, 2, 3]).is_empty()
        False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __getitem__(self, index: int) -> Any:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.
        """
        curr = self._first
        curr_index = 0

        while curr is not None and curr_index < index:
            curr = curr.next
            curr_index += 1

        assert curr is None or curr_index == index

        if curr is None:
            raise IndexError
        else:
            return curr.item

    def __len__(self) -> int:
        """
        :return: The length of the linked list
        >>> len(LinkedList([1,2,3,4]))
        4
        >>> len(LinkedList([]))
        0
        >>> len(LinkedList([1]))
        1
        """
        if self._first is None:
            # Empty Linked List
            return 0
        count = 0
        curr = self._first
        if curr.next == self._first:
            # Only one element
            return 1
        else:
            while curr.next != self._first:
                count += 1
                curr = curr.next
            return count+1

    def delete_player(self, item) -> None:
        """

         item:Item to be deleted
        >>> linky=LinkedList([1,2,3,4,5])
        >>> linky.delete_player(4)
        >>> str(linky)
        '[1 -> 2 -> 3 -> 5]'
        """
        if self._first is None:
            print("Empty linked list")
            return
        curr = self._first
        prev = None
        if curr.item == item:
            #  Remove first node
            #  Delete _first of circular list
            if curr.next == curr:
                #  Only one element of circular list
                self._first = None
            else:
                #  Find last node
                while curr.next != self._first:
                    #  Visit to next node
                    curr = curr.next

                curr.next = self._first.next
                prev = self._first
                self._first = prev.next

        else:
            curr = self._first.next
            #  Find the deleted node
            while curr != self._first:
                if curr.item == item:
                    #  If deleted node found
                    prev.next = curr.next
                    curr = None
                    prev = None
                    break

                prev = curr
                curr = curr.next

            if curr is not None:
                print("\nGiven node is not exist")
