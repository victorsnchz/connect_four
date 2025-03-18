import unittest
import helper_functions
import sys
sys.path.append('src')
from score import Score
from rules import Rules
from bookkeeping import Directions
import helper_functions

class TestRecursiveCount(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.score = Score(Rules())

    def test_count_to_three_all_directions(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_numeric_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name) 

        # include in test file?
        start_row, start_col = 2, 2
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.recursive_count(direction, input_board,
                                                                 start_row, start_col, 
                                                                 0, piece, 
                                                                 visited_slots = set())
            
            self.assertEqual(recursive_count_result, target)
            
    def test_count_to_three_all_directions_borders(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_numeric_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name) 

        # include in test file?
        start_row, start_col = 1, 1
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.recursive_count(direction, input_board,
                                                                 start_row, start_col,
                                                                 0, piece, 
                                                                 visited_slots = set())
            self.assertEqual(recursive_count_result, target)

    def test_count_to_three_backward(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_numeric_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)

        # include in test file?
        start_row, start_col = 3, 3
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.recursive_count(direction, input_board,
                                                                 start_row, start_col,
                                                                 0, piece, 
                                                                 visited_slots = set())
            self.assertEqual(recursive_count_result, target) 

    def test_count_to_three_forward(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_numeric_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name) 

        # include in test file?
        start_row, start_col = 3, 1
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.recursive_count(direction, input_board,
                                                                 start_row, start_col,
                                                                 0, piece, 
                                                                 visited_slots = set())
            self.assertEqual(recursive_count_result, target) 

    def test_count_one(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_numeric_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name) 

        # include in test file?
        start_row, start_col = 1, 1
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.recursive_count(direction, input_board,
                                                                 start_row, start_col,
                                                                 0, piece, 
                                                                 visited_slots = set())
            self.assertEqual(recursive_count_result, target) 

class TestWinCondition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.score = Score(Rules())

    def test_win_all_directions(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_bool_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name) 
        
        start_row, start_col = 3, 2
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.player_wins(input_board,
                                                            start_row, start_col,
                                                            [direction]
                                                            )
            self.assertEqual(recursive_count_result, target) 

    def test_no_win_all_directions(self):

        input_board = helper_functions.get_board_input(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name)
        
        targets = helper_functions.get_bool_targets(self.__class__.__name__,
                                                     sys._getframe().f_code.co_name) 
        
        start_row, start_col = 3, 2
        piece = input_board[start_row][start_col]

        for direction, target in zip(list(Directions), targets):
            
            recursive_count_result = self.score.player_wins(input_board,
                                                            start_row, start_col,
                                                            [direction]
                                                            )
            self.assertEqual(recursive_count_result, target)

if __name__ == '__main__':
    unittest.main()