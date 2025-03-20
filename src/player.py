from bookkeeping import Piece
from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from bot import Bot

class Player:

    def __init__(self, color: Piece, score: int = 0):
        
        self.color = color
        self.score = score

    def increment_score(self):
        self.score += 1

    @abstractmethod
    def next_move(self) -> int:
        pass

    def verify_move(self, move: int) -> None:
        if type(move) != int:
            raise TypeError('Please enter column number as an integer.')
        
class HumanPlayer(Player):
    
    def __init__(self, color: Piece, score = 0):
        super().__init__(color, score)

    def next_move(self) -> int:

        print('Please play your next move.')
        print('Enter column number in which you want to place your pice:')

        user_input = input()

        if not user_input.isnumeric():
            raise TypeError('Please enter a positive integer to indicate column.')
        
        user_input = int(user_input)

        if user_input < 1:
            raise ValueError('Column must be strictly positive.')

        return user_input - 1
        

class BotPlayer(Player):

    def __init__(self, color: Piece, bot: Bot, score = 0):
        super().__init__(color, score)
        self.bot = bot

    def next_move(self):
        pass
