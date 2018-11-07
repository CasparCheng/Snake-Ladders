"""
# Copyright Nick Cheng, 2016
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSCA48, Winter 2017
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from salboard import SALboard
from salbnode import SALBnode

# Add your functions here.

def salb2salbLL(salb):
    ''' (SALboard) -> SALBnode
    Return a linked-list representation of given dictionary
    representation(salb) of a snadder board.
    '''
    # a dictionary maps node index to node object
    all_nodes = dict()
    new_node = None
    # create all squares without snadders
    for i in range(1, salb.numSquares + 1):
        # create a new node and store it into all_nodes
        new_node = SALBnode()
        all_nodes[i] = new_node
        # first square
        if i == 1:
            head = new_node
            previous = new_node
        # all other squares
        else:
            previous.next = new_node
            previous = new_node
    # link last node to head
    new_node.next = head
    # update snadders
    for next_key in salb.snadders:
        source_node = all_nodes[next_key]
        destination_node = all_nodes[salb.snadders[next_key]]
        # option 2: source_node = find_node_by_index(head, next_key)
        # option 2: destination_node = find_node_by_index(head, salb.snadders[next_key])
        source_node.snadder = destination_node
    return head


# option 2:
def find_node_by_index(head, index):
    '''(SALBnode, int) -> SALBnode
    Return nth node in head where n is given index.
    '''
    counter = 1
    result = head
    while counter < index:
        result = result.next
        counter += 1
    return result


def willfinish(first, stepsize):
    '''(SALBnode, int) -> bool
    Return True if the game will terminate, False otherwise.
    first is the first square in a sal board.
    REQ: stepsize is a positive integer
    >>> salb = SALboard(8, {2:5, 7:3})
    >>> first = salb2salbLL(salb)
    >>> willfinish(first, 1)
    False
    >>> willfinish(first, 2)
    False
    >>> willfinish(first, 4)
    True
    >>> willfinish(first, 8)
    True
    >>> willfinish(first, 12)
    True
    >>> willfinish(first, 16)
    True
    '''
    # 1st option: piegeon hole principle
    normal = move(first, None, stepsize)
    slow = first
    # loop through given linked list until all nodes are visited by slow
    # or normal reaches the last node
    while (normal.next is not first) and (slow.next is not first):
        slow = slow.next
        normal = move(first, normal, stepsize)
    # check which pointer reaches the last square
    result = normal.next is first
    '''
    # 2nd option: additional fast pointer
    normal = move(first, None, stepsize)
    fast = move(first, normal, stepsize)
    # determine terminate condition by check if the last square is reached or
    # two pointers meet at a common node
    terminate_condition = meet_or_reach_end(first, fast, normal)
    # loop through given liked list until the last square is reached the or
    # normal and fast meet at a common square
    while not terminate_condition:
        # move fast by stepsize
        fast = move(first, fast, stepsize)
        # re-determine terminate condition by check if the last square is
        # reached or two pointers meet at a common node
        terminate_condition = meet_or_reach_end(first, fast, normal)
        # in case the last square is not reached and two pointers do not
        # meet at a common square
        if not terminate_condition:
            # move fast and normal by another stepsize each
            fast = move(first, fast, stepsize)
            normal = move(first, normal, stepsize)
            # re-determine terminate condition by check if the last square is
            # reached or two pointers meet at a common node
            terminate_condition = meet_or_reach_end(first, fast, normal)
    # result is True if a pointer reaches the last square
    result = (fast.next == first) or (normal.next == first)
    '''
    return result

# option 2:
def meet_or_reach_end(first, fast, normal):
    ''' (SALBnode, SALBnode, SALBnode) -> bool
    Return True if first or normal reaches the last square or they meet at
    a common node.
    '''
    result = False
    # if fast reaches the last square
    if fast.next is first:
        result = True
    # if normal reaches the last square
    elif normal.next is first:
        result = True
    # if normal and fast meet at a common node
    elif normal is fast:
        result = True
    return result


def move(first, starting, stepsize):
    '''(SALBnode, SALBnode, int) -> SALBnode
    Return ending SALBnode given a player's starting node and stepsize.
    REQ: stepsize is a potive integer
    '''
    counter = 0
    # do initial move when player is not on the board
    if starting is None:
        current = first
        counter += 1
    # assume player is on the board
    else:
        current = starting
    # move forward by stepsize, stop moving if stepsize is reached
    while counter < stepsize:
        current = current.next
        counter += 1
    # go to snadder destination
    if current.snadder is not None:
        current = current.snadder
    return current


def whowins(first, step1, step2):
    '''(SALBnode, int, int) -> int
    Return 1 if player 1 wins. Return 2 if player 2 wins or no players are
    not going to reach last square.
    REQ: setp1 and step2 are positive integers.
    >>> salb = SALboard(8, {2:5, 7:3})
    >>> first = salb2salbLL(salb)
    >>> whowins(first, 1, 1)
    2
    >>> whowins(first, 4, 1)
    1
    >>> whowins(first, 2, 4)
    2
    >>> whowins(first, 4, 4)
    1
    >>> whowins(first, 8, 4)
    1
    >>> whowins(first, 4, 8)
    2
    '''
    # if the player 1 will never terminate
    if not willfinish(first, step1):
        result = 2
    # if the player 1 will terminate and player 2 will never terminate
    elif not willfinish(first, step2):
        result = 1
    # assume both players will terminate
    else:
        player1 = move(first, None, step1)
        player2 = move(first, None, step2)
        result = None
        # keep moving player 1 and player 2 respectively until a player
        # reaches the last square
        while result is None:
            # check if player 1 reaches the last square
            if player1.next is first:
                result = 1
            # check if player 2 reaches the last square
            elif player2.next is first:
                result = 2
            # assume no players reach the last square
            else:
                player1 = move(first, player1, step1)
                player2 = move(first, player2, step2)
    return result


def dualboard(first):
    '''(SALBnode) -> SALBnode
    Return the head node of its dual board.
    '''
    old = first
    counter = 1
    # loop through nodes in old linked list until the last node is reached
    # and create all nodes in dual without forward snadders
    while (counter == 1) or (old is not first):
        # create dual_head
        if counter == 1:
            dual_head = SALBnode()
            previous = dual_head
        # create all other nodes
        else:
            new_node = SALBnode()
            previous.next = new_node
            previous = new_node
        # old is the source of a snadder
        if old.snadder and (old.snadder.snadder is None):
            # create a snadder points from destination back to source
            old.snadder.snadder = new_node
            new_node.snadder = old.snadder
        # if old have double-ended arrow with a node in dual board
        elif old.snadder and (old.snadder.snadder is old):
            # create snadder in new linked list
            new_node.snadder = old.snadder
            # remove double-ended link in old
            old.snadder.snadder = None
            old.snadder = None
        # update counter and moves old in original board
        counter += 1
        old = old.next
    # link the last node in dual to its first node
    new_node.next = dual_head

    old = first
    new = dual_head
    # loop through old linked list until the last square is reached
    while old.next is not first:
        # if double-ended arrow is detected
        if old.snadder is not None:
            if old.snadder.snadder is not None:
                # create snadder in new linked list
                new.snadder = old.snadder
                # remove double ended link in old
                old.snadder.snadder = None
                old.snadder = None
        old = old.next
        new = new.next
    return dual_head


