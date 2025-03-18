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
    def next_move(self):
        pass

class HumanPlayer(Player):
    
    def __init__(self, color: Piece, score = 0):
        super().__init__(color, score)

    def next_move(self):
        pass

class BotPlayer(Player):

    def __init__(self, color: Piece, bot: Bot, score = 0):
        super().__init__(color, score)
        self.bot = bot

    def next_move(self):
        pass
