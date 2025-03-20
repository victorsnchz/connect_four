from dataclasses import dataclass, field
from bookkeeping import Directions
import enum

@dataclass(frozen = True)
class GameConfig:
    MIN_ROWS = 6
    MIN_COLS = 6
    MIN_CONNECT = 4
    MIN_WINS = 1

@dataclass(frozen=True)
class Rules:

    columns: int = field(default = GameConfig.MIN_COLS)
    rows: int = field(default =  GameConfig.MIN_ROWS)
    connect_to_win: int =  field(default = GameConfig.MIN_CONNECT)
    versus_human: bool = field(default = True)
    points_to_win: int = field(default=GameConfig.MIN_WINS)
    exclude_directions: set[Directions] = field(default_factory = set) 

    def __post_init__(self):
        self.validate_rules()

    def validate_rules(self):
        
        if type(self.rows) is not int:
            raise TypeError(f'rows must be int not {type(self.rows)}')

        if self.rows < GameConfig.MIN_ROWS:
            raise ValueError(f'rows must be at least {GameConfig.MIN_ROWS}')
        
        if type(self.columns) is not int:
            raise TypeError(f'columns must be int not {type(self.columns)}')
        
        if self.columns < GameConfig.MIN_COLS:
            raise ValueError(f'columns must be at least {GameConfig.MIN_COLS}')

        if type(self.connect_to_win) is not int:
            raise TypeError('connect to win must be int not ',
                            f'{type(self.connect_to_win)}')

        if self.connect_to_win < GameConfig.MIN_CONNECT:
            raise ValueError('connect to win must be at least ',
                             f'{GameConfig.MIN_CONNECT}')

        if type(self.versus_human) is not bool:
            raise TypeError('versus human must be bool not ',
                            f'{type(self.versus_human)}')
        
        if type(self.points_to_win) is not int:
            raise TypeError('points to win must be bool not', 
                            f'{type(self.points_to_win)}')
        
        if self.points_to_win < GameConfig.MIN_WINS:
            raise ValueError('points to win must be greater or equal to ',
                             f'{GameConfig.MIN_WINS}') 
        
        if type(self.exclude_directions) is not set:
            raise TypeError(f'excluded directions must be contained in a set') 

        if self.exclude_directions and \
            any(type(direction) for direction in self.exclude_directions) \
                is not Directions:
            raise TypeError(f'excluded directions must only contain Direction objects')