from bookkeeping import Piece, Directions
from rules import Rules, GameConfig
from collections import defaultdict
from score import Score

class Board:
    def __init__(self, rules: Rules, grid: list[list[Piece]] = None ):

        self._rules = rules
        
        if grid is not None and self.is_valid_grid(grid):
            self.grid = grid
            self.free_slot_in_columns = \
                {col: self.find_free_slot_in_columns(col) for col in range(len(self.grid[0]))}
        else:
            self.grid = self.make_grid()
            self.free_slot_in_columns = \
                {i : len(self.grid) for i in range(len(self.grid))}

    def make_grid(self) -> list[list[Piece]]:
        return [[Piece.EMPTY for _ in range(self._rules.columns)] 
                for _ in range(self._rules.rows)]

    def is_valid_grid(self, grid):
        # min 6 rows 6 cols
        if len(grid) < GameConfig.MIN_ROWS:
            raise UserWarning(f'Grid does not meet minimum size conditions: \
                              {GameConfig.MIN_ROWS} rows.')
        
        if len(grid[0]) < GameConfig.MIN_COLS:
            raise UserWarning(f'Grid does not meet minimum size conditions: \
                              {GameConfig.MIN_ROWS} rows.')
        
        if len(set([len(row) for row in grid])) > 1:
            raise UserWarning(f'Grid rows should all have same size.')
        
        score = Score(rules=self._rules)
        if score.is_grid_already_winning(grid):
            raise UserWarning(f'Grid already contains a winning connect.')

        # no empty-cell below a non-empty-cells
        top_row = grid[0]
        for row in grid[1:]:
            for top, bottom in zip(top_row, row):
                if bottom == Piece('E') != top: 
                    raise UserWarning('There must be no empty cell below a full cell.')
                top_row = row

        valid_pieces = set(piece for piece in Piece)
        for row in grid:
            invalid_pieces = [piece not in valid_pieces for piece in row]
            if any(invalid_pieces):
                invalid = [piece for piece, is_invalid in zip(row, invalid_pieces) 
                           if is_invalid]
                conjugate = 'are not ' if len(invalid) > 1 else 'is not'
                raise UserWarning(f'{invalid} {conjugate} a valid piece') 

        return True




    def find_free_slot_in_columns(self, col: int) -> int:

        """ Find first filled cell in column.

        Uses a classic binary search method along each grid column.
        Complexity O(mlogn).
        Only called once as updates then take place in a dict.
        """

        bottom_idx = len(self.grid) - 1
        top_idx = 0
        
        idx = (bottom_idx + top_idx) // 2
        
        while(bottom_idx > top_idx):

            if(self.grid[idx][col] == Piece.EMPTY != self.grid[idx + 1][col]):
                return idx + 1
            
            if(self.grid[idx][col] == Piece.EMPTY == self.grid[idx + 1][col]):
                top_idx = idx + 1

            if(self.grid[idx][col] != Piece.EMPTY != self.grid[idx + 1][col]):
                bottom_idx = idx
            
            idx = (bottom_idx + top_idx) // 2

        return idx + 1

    def add_piece(self, piece: Piece, grid: list[list[Piece]], col: int) -> bool:
        
        if self.is_grid_full():
            raise ValueError('Grid is full. Please start a new game.')
            
        if self.free_slot_in_columns[col] > 0:
            free_columns = [col for col, count in self.free_slot_in_columns 
                            if count > 0]
            error_msg = f'This column is full, you may try columns {free_columns}.'
            raise ValueError(error_msg)
        
        free_row = len(self.grid) - self.self.free_slot_in_columns[col]
        grid[free_row][col] = piece
        self.self.free_slot_in_columns[col] -= 1

    def is_grid_full(self):
        return not all(self.free_slot_in_columns.values()) 

    def display(self) -> None:
        pass