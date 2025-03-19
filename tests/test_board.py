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
                                     board.free_slot_in_columns.values()): 
            
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

    def test_intruder(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        
        input_grid[3][3] = 'I'
        with self.assertRaises(UserWarning):
            board = Board(Rules(), grid = input_grid)

    def test_first_free_slot_in_columns(self):
        input_grid = \
            helper_functions.get_board_input(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        targets = \
            helper_functions.get_numeric_targets(test_case=self.__class__.__name__,
                                             test_name=sys._getframe().f_code.co_name)
        
        board = Board(Rules(), grid = input_grid)
        for counter, target in zip(board.free_slot_in_columns,
                                   targets):
            self.assertEqual(counter, target)
        
    
    @unittest.SkipTest
    def test_is_grid_full(self):
        pass
    pass

class TestBoardChanges(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        rules = Rules()
        cls.board = Board(rules)

    @unittest.SkipTest
    def test_add_piece(self):
        pass
    
    pass

class TestFullBoard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        custom_grid = helper_functions.get_board_input(test_case=cls.__class__.__qualname__)
        rules = Rules()
        cls.board = Board(rules)
    
    @unittest.SkipTest
    def test_is_grid_full(self):
        self.assertEqual(self.board.is_grid_full(), True)

    @unittest.SkipTest
    def test_add_piece(self):
        with AssertionError(ValueError):
            self.board.add_piece(Piece('R'))
        
    @unittest.SkipTest
    def test_free_col_counter(self):
        free_columns = sum(self.board.free_slot_in_columns.values)
        self.assertEqual(free_columns, 0)

if __name__ == '__main__':
    unittest.main() 