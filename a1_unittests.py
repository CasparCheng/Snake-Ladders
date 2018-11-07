import unittest
from salbnode import *
from salboard import *
from salbLLfunctions import *

# enable if you want to visualize results of dualboard
enable_logging_display = True


class Test_a1(unittest.TestCase):

    def test_type_salb2salbLL(self):
        original = SALboard(1, {})
        match = SALBnode()

        id = salb2salbLL(original)

        self.assertEqual(type(id), type(
            match), "Err type, salb2salbLL() must return a SALBnode, not " +
                     str(type(id)))

    def test_00_salb2salbLL_empty(self):
        original = SALboard(1, {})
        id = 'len of board is 1 []'

        match = self.id_salbnode(salb2salbLL(original))

        self.assertEqual(id, match, "Err 00'" + id +
                         "' is not '" + match + "'")

    def test_01_salb2salbLL_three_loop(self):
        original = SALboard(3, {1: 2, 2: 1})
        id = 'len of board is 3 [1:2, 2:1]'

        match = self.id_salbnode(salb2salbLL(original))

        self.assertEqual(id, match, "Err 01'" + id +
                         "' is not '" + match + "'")

    def test_02_salb2salbLL_long_empty(self):
        original = SALboard(553, {})
        id = 'len of board is 553 []'

        match = self.id_salbnode(salb2salbLL(original))

        self.assertEqual(id, match, "Err 02'" + id +
                         "' is not '" + match + "'")

    def test_03_salb2salbLL_every_snadder(self):
        original = SALboard(7, {1: 2, 2: 3, 3: 4, 4: 5, 5: 6})
        id = 'len of board is 7 [1:2, 2:3, 3:4, 4:5, 5:6]'

        match = self.id_salbnode(salb2salbLL(original))

        self.assertEqual(id, match, "Err 03'" + id +
                         "' is not '" + match + "'")

    def test_04_salb2salbLL_long_confusing(self):
        original = SALboard(
            47, {1: 43, 9: 8, 4: 7, 21: 3, 18: 19, 6: 35, 19: 20, 20: 44})
        id = 'len of board is 47 [1:43, 4:7, 6:35, 9:8, 18:19, 19:20, 20:44, 21:3]'

        match = self.id_salbnode(salb2salbLL(original))

        self.assertEqual(id, match, "Err 04'" + id +
                         "' is not '" + match + "'")

    def test_05_salb2salbLL_long_confusing(self):
        original = SALboard(
            10, {1: 2, 2: 3, 7: 4, 8: 9})
        id = 'len of board is 10 [1:2, 2:3, 7:4, 8:9]'

        match = self.id_salbnode(salb2salbLL(original))

        self.assertEqual(id, match, "Err 04'" + id +
                         "' is not '" + match + "'")


    # salb2salbLL testing ends ---

    def test_type_willfinish(self):
        original = salb2salbLL(SALboard(3, {}))

        match = willfinish(original, 1)

        self.assertEqual(type(True), type(
            match), "Err type, wilfiinsh() must return a bool, not " +
                     str(type(match)))

    def test_00_willfinish(self):
        original = salb2salbLL(SALboard(12, {5: 3, 3: 4, 7: 2}))
        match = [False, True, True, True, False]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 00 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_01_willfinish(self):
        original = salb2salbLL(SALboard(9, {2: 5, 8: 4, 6: 7}))
        match = [False, True, False, False, True]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 01 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_02_willfinish(self):
        original = salb2salbLL(SALboard(11, {8: 5, 2: 7, 6: 9}))
        match = [True, True, False, True, False]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 02 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_03_willfinish(self):
        original = salb2salbLL(SALboard(7, {2: 4, 6: 3}))
        match = [False, True, False, False, False]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 03 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_04_willfinish(self):
        original = salb2salbLL(SALboard(10, {}))
        match = [True, True, True, True, True]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 04 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_05_willfinish(self):
        original = salb2salbLL(SALboard(4, {1: 2, 2: 3}))
        match = [True, True, False, True, True]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 05 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_06_willfinish(self):
        original = salb2salbLL(SALboard(3, {}))
        match = [True, True, True, True, True]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 06 ' +
                         str(match) + ' is not results: ' + str(results))

    def test_07_willfinish(self):
        original = salb2salbLL(SALboard(1, {}))
        match = [True, True, True, True, True]

        results = []

        step_sizes = [1, 2, 3, 4, 5]
        for step in step_sizes:
            results.append(willfinish(original, step))

        self.assertEqual(results, match, 'Err 07 ' +
                         str(match) + ' is not results: ' + str(results))

    # willfinish testing ends ---

    def test_00_whowins(self):
        original = salb2salbLL(SALboard(11, {8: 5, 2: 7, 6: 9}))
        self.assertEqual(whowins(original, 2, 3), 1)

    def test_01_whowins(self):
        original = salb2salbLL(SALboard(11, {8: 5, 2: 7, 6: 9}))
        self.assertEqual(whowins(original, 3, 2), 2)

    def test_02_whowins(self):
        original = salb2salbLL(SALboard(11, {8: 5, 2: 7, 6: 9}))
        self.assertEqual(whowins(original, 3, 3), 2)

    def test_03_whowins(self):
        original = salb2salbLL(SALboard(11, {8: 5, 2: 7, 6: 9}))
        self.assertEqual(whowins(original, 2, 2), 1)

    def test_04_whowins(self):
        original = salb2salbLL(SALboard(11, {10: 3}))
        self.assertEqual(whowins(original, 1, 2), 2)

    def test_05_whowins(self):
        original = salb2salbLL(SALboard(11, {10: 3}))
        self.assertEqual(whowins(original, 2, 1), 1)

    ## whowins testing ends ---

    def test_00_dualboard(self):
        board = salb2salbLL(SALboard(10, {1: 2, 2: 3, 7: 4, 8: 9}))
        d_dual = dualboard(dualboard(board))

        id = self.id_salbnode(board)
        match = self.id_salbnode(d_dual)

        if enable_logging_display:
            print("Original baord: '" + id +
                  "' resultant board: '" + match + "'")

        self.assertEqual(id, match, 'Given: ' + id +
                         ' is not same as result: ' + match)

    def test_01_dualboard(self):
        board = salb2salbLL(SALboard(9, {1: 7, 7: 8}))
        d_dual = dualboard(dualboard(board))

        id = self.id_salbnode(board)
        match = self.id_salbnode(d_dual)

        if enable_logging_display:
            print("Original baord: '" + id +
                  "' resultant board: '" + match + "'")

        self.assertEqual(id, match, 'Given: ' + id +
                         ' is not same as result: ' + match)

    def test_02_dualboard_empty_direct(self):
        board = salb2salbLL(SALboard(9, {}))
        d_dual = dualboard(dualboard(board))

        id = 'len of board is 9 []'
        match = self.id_salbnode(d_dual)

        if enable_logging_display:
            print("Original baord: '" + id +
                  "' resultant board: '" + match + "'")

        self.assertEqual(id, match, 'Given: ' + id +
                         ' is not same as result: ' + match)

    def test_03_dualboard(self):
        board = salb2salbLL(
            SALboard(21, {1: 7, 7: 8, 12: 3, 5: 13, 19: 20, 4: 6}))
        d_dual = dualboard(dualboard(board))

        id = self.id_salbnode(board)
        match = self.id_salbnode(d_dual)

        if enable_logging_display:
            print("Original baord: '" + id +
                  "' resultant board: '" + match + "'")

        self.assertEqual(id, match, 'Given: ' + id +
                         ' is not same as result: ' + match)

    # dualboard testing ends ---

    def id_salbnode(self: 'Test_a1', head: 'SALBnode') -> str:
        ''' Given a linked list representation of a game board,
        creates a unique identifier string representation of snadders.
        This is an extra function only used for testing. NOT to be marked.

        Format of id string is:
        "len of board is <int> [int:int, int:int, <...> , int:int]"
        '''
        # for storing list of nodes
        list_nodes = []

        # set current node head
        curr_node = head
        list_nodes.append(curr_node)
        curr_node = curr_node.next

        snadder_counter = 0
        # add all nodes to list
        while curr_node is not head:
            list_nodes.append(curr_node)
            curr_node = curr_node.next

        str_to_ret = 'len of board is ' + str(len(list_nodes)) + ' ['

        # loop through each snadder source, and find destination
        for i in range(0, len(list_nodes)):
            if list_nodes[i].snadder is not None:
                # format string to be returned
                str_to_ret += str(i + 1) + ':'  # source
                d_ind = list_nodes.index(list_nodes[i].snadder)
                str_to_ret += str(d_ind + 1) + ', '  # destination
                # increment snadder counter
                snadder_counter += 1

        if snadder_counter > 0:
            # trim the string, if more than one snadder found (formatting)
            str_to_ret = str_to_ret[0: len(str_to_ret) - 2]

        # return the formatted substring
        return str_to_ret + ']'

if(__name__ == "__main__"):
    unittest.main(exit=False)
