import unittest
import sys

sys.path.append('src')
from rules import Rules
from board import Board
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
                                     board.columns_free_positions_counter.values()): 
            
            self.assertEqual(col_count, target)

    def test_is_grid_full(self):
        board = Board(self.rules)
        self.assertEqual(board.is_grid_full(), False)

class TestBoardCustomInitialization(unittest.TestCase):
    pass

class TestBoardChanges(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()