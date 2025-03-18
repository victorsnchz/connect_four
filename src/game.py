from rules import Rules
from bookkeeping import Piece
from player import HumanPlayer, BotPlayer, Player
from board import Board


class Game:
    def __init__(self, rules: Rules, board: Board = None):
        
        self._rules = rules

        if self.board is None:
            self.board = self.make_board()

        if self._rules.versus_human:
            self.players = self.make_human_players()
        else:
            self.players = self.make_human_and_machine_players()

        self.scoreboard = [player.score for player in self.players]

    def make_board(self):
        return Board(self._rules)

    def make_players(self) -> tuple[Player]:
        player1 = HumanPlayer(Piece.RED)
        player2 = HumanPlayer(Piece.YELLOW)
        return player1, player2

    def make_human_and_machine_players(self) -> tuple[Player]:
        
        player1 = HumanPlayer(Piece.RED)
        player2 = BotPlayer(Piece.YELLOW)
        
        return player1, player2
    
    def play(self) -> None:

        while max(self.scoreboard) < self._rules.points_to_win:
            self.play_round()
            pass

        print(f'Player {0} WINS!')
        print(f'Final score: ')
        print(f'Player 1: {0} {"*" * 40} Player 2: {0}')
        print('Congratulations!!!')

    def play_round(self) -> None:
        pass

