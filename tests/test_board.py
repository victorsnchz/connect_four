import unittest
import sys

sys.path.append('src')
from rules import Rules
from board import Board
from bookkeeping import Piece
import helper_functions

class TestBoardDefaultInitialization(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rules = Rules()

    def test_default_grid(self):
        
        board = Board(self.rules)
        grid = board.grid
        target = \
            helper_functions.get_board_target(test_case=self.__class__.__name__,
                                              test_name=sys._getframe().f_code.co_name)

        self.assertEqual(grid, target)

    def test_free_col_counter(self):
        
        board = Board(self.rules)
        targets = \
            helper_functions.get_numeric_targets(test_case=self.__class__.__name__,
                                               test_name=sys._getframe().f_code.co_name)

        for target, col_count in zip(targets, 
                                     board.free_index_in_columns.values()): 
            
            self.assertEqual(col_count, target)

    def test_is_grid_full(self):
        board = Board(self.rules)
        self.assertEqual(board.is_grid_full(), False)

class TestBoardCustomInitialization(unittest.TestCase):
    
    def test_valid_grid(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), grid = input_grid)
        self.assertEqual(board.grid, input_grid)

    def test_invalid_grid_rows(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid = input_grid)
    
    def test_invalid_grid_cols(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid = input_grid)

    def test_invalid_grid_consitency_rows(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid = input_grid)

    def test_invalid_grid_missing_piece(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid = input_grid)

    def test_invalid_grid_already_winning(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid=input_grid)

    def test_intruder(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        
        input_grid[3][3] = 'I'
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid = input_grid)

    def test_free_index_in_columns(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        targets = \
            helper_functions.get_numeric_targets(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        
        board = Board(Rules(), grid = input_grid)
        for counter, target in zip(board.free_index_in_columns.values(),
                                   targets):
            self.assertEqual(counter, target)
        
    def test_is_grid_full(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), grid = input_grid)
        self.assertEqual(board.is_grid_full(), False)

class TestBoardChanges(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        custom_grid = \
            helper_functions.get_board_input(test_case='TestBoardChanges',
                                             test_name=sys._getframe().f_code.co_name)
        cls.board = Board(Rules(), grid = custom_grid)

    def test_add_piece(self):
        self.board.add_piece(Piece('R'), col = 1)
        target = \
            helper_functions.get_board_target(test_case=self.__class__.__name__,
                                              test_name=sys._getframe().f_code.co_name)
        self.assertEqual(self.board.grid, target)

class TestFullBoard(unittest.TestCase):
    
    def test_full_grid(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), input_grid)
        self.assertEqual(board.is_grid_full(), True)

    def test_add_piece(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), input_grid)
        
        with self.assertRaises(ValueError):
            board.add_piece(Piece('R'), col = 0)

    def test_free_index_in_columns(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), input_grid)
        free_columns = sum(board.free_index_in_columns.values())
        self.assertEqual(free_columns, -6)

    def test_one_free_col(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), input_grid)
        self.assertEqual(board.is_grid_full(), False)

    def test_one_free_row(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), input_grid)
        self.assertEqual(board.is_grid_full(), False)

    def test_one_free_slot(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        board = Board(Rules(), input_grid)
        self.assertEqual(board.is_grid_full(), False)    

if __name__ == '__main__':
    unittest.main() 