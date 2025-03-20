import sys
sys.path.append('tests/')
import helper_functions

from board import Board
from rules import Rules
from bookkeeping import Piece

def main():
    
    grid = helper_functions.read_file_as_board('tests/data/TestBoardCustomInitialization/inputs/test_valid_grid.txt')
    board = Board(Rules(), grid)

    board.display()

    board.add_piece(Piece('R'), 1)
    # board.add_piece(Piece('R'), 1)
    #board.add_piece(Piece('R'), 1)

    board.display()

if __name__ == '__main__':
    main()