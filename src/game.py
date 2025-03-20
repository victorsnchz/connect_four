from rules import Rules
from bookkeeping import Piece
from player import HumanPlayer, BotPlayer, Player
from board import Board
from score import Score

import copy


class Game:
    def __init__(self, rules: Rules, board: Board = None):
        
        self._rules = rules

        if board is None:
            self.board = self.make_board()

        if self._rules.versus_human:
            self.players: tuple[Player] = self.make_human_players()
        else:
            self.players: tuple[Player] = self.make_human_and_machine_players()

        self.scoreboard: tuple[int] = self.update_scoreboard()

    def make_board(self):
        return Board(self._rules)

    def make_human_players(self) -> tuple[Player]:
        player1 = HumanPlayer(Piece.RED)
        player2 = HumanPlayer(Piece.YELLOW)
        return player1, player2

    def make_human_and_machine_players(self) -> tuple[Player]:
        
        player1 = HumanPlayer(Piece.RED)
        player2 = BotPlayer(Piece.YELLOW)
        
        return player1, player2
    
    def update_scoreboard(self) -> tuple[int]:
        return (player.score for player in self.players)
    
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

    def play_round(self):
        
        board = copy.deepcopy(self.board)
        round_score = Score(self._rules)

        keep_playing = True
        player_index = 0

        board.display()

        while(keep_playing):
            
            player_index = (player_index + 1) % len(self.players)

            player: Player = self.players[player_index]

            col = player.next_move()
            board.add_piece(Piece(player.color), col)

            board.display()

            # TODO
            # encapsulate into board (eg. last played cell or something)
            row = board.free_index_in_columns[col] + 1

            player_wins_round = round_score.player_wins(board.grid, 
                                                        *board.get_last_played_move())

            keep_playing = not (board.is_grid_full() or player_wins_round)

        if player_wins_round:
            player.increment_score()
            self.scoreboard = self.update_scoreboard()
            print(f'Player {player.color} wins this round!')
            return
        
        print('NULL!')
        return