from bookkeeping import Piece, Directions
from rules import Rules
from collections import defaultdict

class Board:
    def __init__(self, rules: Rules, grid: list[list[Piece]] = None ):

        self._rules = rules
        
        self.grid = self.make_grid() if grid is None else grid

        self.columns_free_positions_counter = \
            self.initialize_columns_free_positions_counter()

    def make_grid(self) -> list[list[Piece]]:
        return [[Piece.EMPTY for _ in range(self._rules.columns)] 
                for _ in range(self._rules.rows)]
    
    def initialize_columns_free_positions_counter(self):

        return {i : len(self.grid[0]) for i in range(len(self.grid))}

        return defaultdict(lambda: len(self.grid[0]) - 1)
        # TODO
        # fix for user-provided grid (not necessarily empty)
        # intuitively would use a binary search to locate first empty row in each column
        # O(m * logn) for m x n grid 
        # (good to know but irrelevant except if user plays on a 10^6 x 10^6 grid)
        return defaultdict(int)

    def add_piece(self, piece: Piece, grid: list[list[Piece]], col: int) -> bool:
        
        # remark
        # this condition should NEVER have to return true
        # if this returns true it means higher-level functions try to insert piece into
        # a full grid instead of stopping the game => check condition higher up
        # log and raise error
        if self.is_grid_full():
            print('Grid is full, start a new game.')

        if self.columns_free_positions_counter[col] > 0:
            print('This column is full, please try another one.')
            free_columns = [col for col, count in self.columns_free_positions_counter 
                            if count > 0]
            print(f'Free columns are {free_columns}')
        
        free_row = len(self.grid) - self.self.columns_free_positions_counter[col]
        grid[free_row][col] = piece
        self.self.columns_free_positions_counter[col] -= 1

    def is_grid_full(self):
        return not all(self.columns_free_positions_counter.values()) 

    def display(self) -> None:
        pass