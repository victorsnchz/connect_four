from rules import Rules
from bookkeeping import Directions, Piece

class Score:

    def __init__(self, rules: Rules):
        self._rules = rules

    def direction_increments_forward(self, row: int, col: int,
                            direction: Directions) -> tuple[int, int]:
        if direction.name == 'HORIZONTAL':
            return row, col + 1
        if direction.name == 'VERTICAL':
            return row + 1, col
        if direction.name == 'DIAGONAL_UP':
            return row - 1, col + 1
        if direction.name == 'DIAGONAL_DOWN':
            return row + 1, col + 1
    
    def direction_increments_backward(self, row: int, col: int,
                            direction: Directions) -> tuple[int, int]:
        if direction.name == 'HORIZONTAL':
            return row, col - 1
        if direction.name == 'VERTICAL':
            return row - 1, col
        if direction.name == 'DIAGONAL_UP':
            return row + 1, col - 1
        if direction.name == 'DIAGONAL_DOWN':
            return row - 1, col - 1

    def recursive_count(self, direction: Directions, grid: list[list[Piece]], 
                        row: int, col: int, count: int, 
                        piece: Piece, visited_slots) -> int:
            
        if (row < 0 or col < 0 
            or row >= len(grid) or col >= len(grid[0]) 
            or grid[row][col] != piece
            ):
            
            return count
        
        count += 1
        visited_slots.add((row, col))

        fwd_row, fwd_col = self.direction_increments_forward(row, col, direction)
        
        if (fwd_row, fwd_col) not in visited_slots:
            count = self.recursive_count(direction, grid,
                                         fwd_row, fwd_col, 
                                         count, piece, visited_slots)
            
        bwd_row, bwd_col = self.direction_increments_backward(row, col, direction)
        
        if(bwd_row, bwd_col) not in visited_slots:
            count = self.recursive_count(direction, grid, 
                                         bwd_row, bwd_col,
                                         count,  piece, visited_slots)

        return count
    
    def player_wins(self, grid: list[list[Piece]], row: int, col: int) -> bool:
        
        piece = grid[row][col]

        for direction in \
            set(Directions).symmetric_difference(self._rules.exclude_directions):
            
            visited_slots = set()
            if self.recursive_count(direction, grid, row, col, 0, 
                                    piece, visited_slots) >= self._rules.connect_to_win:
                return True
        
        return False
    
    def is_grid_already_winning(self, grid):
        score = Score(self._rules)

        for direction in set(Directions).symmetric_difference(
            self._rules.exclude_directions
        ):
            visited_slots = set()
            
            for row in range(len(grid)):
                for col in range(len(grid[0])):    
                    piece = grid[row][col]
                    
                    if (row, col) not in visited_slots \
                        and piece != Piece.EMPTY \
                        and self.recursive_count(
                                direction, grid, row, col, 0, piece, visited_slots
                            ) >= self._rules.connect_to_win:
                        
                        return True
                    
        return False
                        
