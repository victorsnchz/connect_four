import sys
sys.path.append('tests/')
import helper_functions

from board import Board
from rules import Rules
from bookkeeping import Piece
from game import Game

def main():
    
    game = Game(Rules())

    game.play()

if __name__ == '__main__':
    main()