"""
# Copyright Nick Cheng, Jiyuan Cheng 2016
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


def circular_linked_list(head):
    '''(SALBnode) -> SALBnode
    Given a head node, the function create a circular linked list
    Return the head of this circular linked list.
    '''
    # define a current node equal to head
    curr = head
    # loop the given linked list until the last node is found
    while curr.next is not None:
        # let current be next node
        curr = curr.next
    # connect the last node to head node
    curr.next = head
    return head


def find_start_node(first, stepsize):
    '''(SALBnode, int) -> SALBnode
    Given a circular linked list and a step size, the function finds the start
    node according to the step size
    Return the start node
    '''
    # assume the step size is 1
    if stepsize == 1:
        # the start node is the first node in this linked list
        start_node = first
    # otherwise
    else:
        # let start node be first node
        start_node = first
        # using counter equal to 1
        counter = 1
        # loop the linked list from start node until counter >= stepsize
        while counter < stepsize:
            # move to next node
            start_node = start_node.next
            # update the counter
            counter += 1
    # if there is a snadder in this node
    if start_node.snadder is not None:
        # move to the snadder node
        start_node = start_node.snadder
    return start_node


def move_steps(start_node, stepsize):
    '''(SALBnode, int) -> SALBnode
    Given a start node in this linked list and a step size, the function let
    the player move the steps according to the step size from start node
    '''
    # let current be start node
    curr = start_node
    # using counter equal to 0
    counter = 0
    # loop the linked list until counter >= stepsize
    while counter < stepsize:
        # move to next node
        curr = curr.next
        # update counter
        counter += 1
    # if there is a snadder in this node
    if curr.snadder is not None:
        # current move to the snadder node
        curr = curr.snadder
    return curr


def copy_linked_list(first):
    '''(SALBnode) -> SALBnode
    Given a circular linked list, the function make a copy to this linked
    list without snadder
    '''
    # create a node dictionary
    node_dict = {}
    # define old is first
    old = first
    # number of node is 1
    num_node = 1
    # loop the given linked list until find the last node
    while old.next != first:
        # move to next node
        old = old.next
        # update number nodes
        num_node += 1
    # loop the number of nodes
    for i in range(1, num_node + 1):
        # create a new node
        new_node = SALBnode()
        # put it to the node dictionary
        node_dict[i] = new_node
        # if i is 1
        if i == 1:
            # new_node is the first node
            head = new_node
            # let previous node be the first node
            prev = new_node
        # otherwise:
        else:
            # previous node's next node is the new node
            prev.next = new_node
            # update the previous node
            prev = new_node
    # let the new linked list be circular
    head = circular_linked_list(head)
    # define curr is new linked list head
    curr = head
    # old updates for the original linked list head
    old = first
    # loop the old linked list and the new linked list until they both reach
    # the last squares
    while old.next != first and curr.next != first:
        # if the node of old has snadder
        if old.snadder is not None:
            # node of curr links the snadder node too
            curr.snadder = old.snadder
        # move to next old node
        old = old.next
        # move to next new node
        curr = curr.next
    return head


def salb2salbLL(salb):
    '''(SALboard) -> SALBnode
    Given a snakes and ladders board which is a dictionary, the function
    transfer this board to the linked list type.
    Return the same board as a linked list
    '''
    # create a empty dictionary for nodes
    nodes = {}
    # loop the number of squares
    for n in range(1, salb.numSquares + 1):
        # create a new node
        node = SALBnode()
        # every time store the new node as value using the current n as key
        nodes[n] = node
        # if n euqual to 1
        if n == 1:
            # it is the first node
            head = node
            # let the current node be previous node
            prev = node
        # otherwise
        else:
            # previous node's next node is new_node
            prev.next = node
            # update the previous node as the new_node
            prev = node
    # let the current linked list be a circular linked list
    head = circular_linked_list(head)
    # loop the source node in the snadders dictionary
    for source in salb.snadders:
        # match the node in the node dictionary
        from_node = nodes[source]
        # get the number of destination node
        destination = salb.snadders[source]
        # get the node of destination
        to_node = nodes[destination]
        # let the source node's snadder be the node of destination
        from_node.snadder = to_node
    return head


def willfinish(first, stepsize):
    '''(SALBnode, int) -> bool
    Given a linked list which represents a snakes and ladders board, and one
    step size. The function justifies whether a player can ever arrive the
    last square through using the given step size.
    Return a boolean statement.

    REQ: one square only can be the source of one snadder.
    REQ: one square only can be the destination of one snadder.
    REQ: the last square can not be the source or the destination of a snadder.
    REQ: stepsize > 0

    >>> first = salb2salbLL(SALboard(1, {}))
    >>> stepsize = 2
    >>> willfinish(first, stepsize)
    True
    >>> first = salb2salbLL(SALboard(4, {1: 2, 2: 3}))
    >>> stepsize = 3
    >>> willfinish(first, stepsize)
    False
    >>> first = salb2salbLL(SALboard(9, {2: 5, 8: 4, 6: 7}))
    >>> stepsize = 5
    >>> willfinish(first, stepsize)
    True
    '''
    # let original node node equal to first node
    origin = first
    # current node is the start node according to the stepsize
    curr_node = find_start_node(first, stepsize)
    # loop the original linked list and the current linked list from start node
    # until current node reach the last node or original node reach the last
    # node
    while (curr_node.next != first) and (origin.next != first):
        # let original node move to next
        origin = origin.next
        # current node move to next node according to the given stepsize
        curr_node = move_steps(curr_node, stepsize)
    # judge whether the current node have reached the last node
    return curr_node.next == first


def whowins(first, step1, step2):
    '''(SALBnode, int, int) -> int
    Given a linked list which represents a snakes and ladders board, one
    step size for player1 and one step size for player2. The first player who
    can move to the last square wins the game, and if they both cannot move
    to the last square then the player2 will be considered win.
    Return the number of player who wins this game.

    >>> first = salb2salbLL(SALboard(4, {1: 2, 2: 3}))
    >>> step1 = 2
    >>> step2 = 3
    >>> whowins(first, step1, step2)
    1
    >>> first = salb2salbLL(SALboard(9, {2: 5, 8: 4, 6: 7}))
    >>> step1 = 1
    >>> step2 = 5
    >>> whowins(first, step1, step2)
    2
    >>> first = salb2salbLL(SALboard(11, {8: 5, 2: 7, 6: 9}))
    >>> step1 = 3
    >>> step2 = 4
    2
    '''

    # judge whether player1 can finish the game
    estimate_p1 = willfinish(first, step1)
    # judge whether player2 can finish the game
    estimate_p2 = willfinish(first, step2)
    # if they both can finish the game
    if estimate_p1 and estimate_p2:
        # find where the player1 start
        p1_start_node = find_start_node(first, step1)
        # find where the player2 start
        p2_start_node = find_start_node(first, step2)
        # let current node be the player 1 start node
        curr_p1 = p1_start_node
        # let current node be the player 2 start node
        curr_p2 = p2_start_node
        # from 1 as start node for player 1
        move_p1 = 1
        # from 1 as start node for player 2
        move_p2 = 1
        # loop the linked list from player 1 start node until it reach the
        # last node
        while curr_p1.next != first:
            # move to next node
            curr_p1 = move_steps(curr_p1, step1)
            # count move step for player 1
            move_p1 += 1
        # loop the linked list from player 2 start node until it reach the
        # last node
        while curr_p2.next != first:
            # move to next node
            curr_p2 = move_steps(curr_p2, step2)
            # count move step for player 2
            move_p2 += 1
        # if the move steps of player 1 is bigger than player 2
        if move_p1 > move_p2:
            # player 2 wins
            win = 2
        # else if move steps of player 2 is bigger than player 1
        elif move_p2 > move_p1:
            # player 1 wins
            win = 1
        # other wise
        else:
            # player 1 wins
            win = 1
    else:
        # if player 1 can finish game and player 2 cannot
        if estimate_p1:
            # player 1 wins
            win = 1
        # else if player 2 can finish game an player 1 cannot
        elif estimate_p2:
            # player 2 wins
            win = 2
        # if they both cannot finish
        else:
            # player2 wins
            win = 2

    return win


def dualboard(first):
    '''(SALBnode) -> SALBnode
    Given a linked list which represents a snakes and ladders board, then do
    its dual which means the source and the destination of every snadder will
    be exchanged.
    Return the new linked list

    REQ: the new linked list has the same number of squares and snadders
    REQ: the inputed linked list will not be changed
    '''

    # let old be the first node
    old = first
    # make it copy
    new_node = copy_linked_list(first)
    # loop the old linked list until they reach the last square
    while old.next != first and new_node.next != first:
        # if the node has snadder
        if (old.snadder is not None):
            # exchange the new node snadder point
            new_node.snadder.snadder = new_node
        # move to next old node
        old = old.next
        # move to next new node
        new_node = new_node.next

    return new_node
