import enum

class Piece(enum.Enum):
    EMPTY = 'E'
    RED = 'R'
    YELLOW = 'Y'

class Directions(enum.Enum):
    HORIZONTAL = 'H'
    VERTICAL = 'V'
    DIAGONAL_UP = 'DU'
    DIAGONAL_DOWN = 'DV'