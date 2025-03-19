from dataclasses import dataclass, field
from bookkeeping import Directions
import enum

@dataclass(frozen=True)
class Rules:

    columns: int = field(default = 6)
    rows: int = field(default = 6)
    connect_to_win: int =  field(default = 4)
    versus_human: bool = field(default = True)
    points_to_win: int = field(default=1)
    exclude_directions: set[Directions] = field(default = set) 

    def __post_init__(self):
        self.validate_rules()

    def validate_rules(self):
        
        if type(self.columns) is not int:
            raise TypeError(f'columns must be int not {type(self.columns)}')
        
        if self.columns < GameConfig.MIN_COLS:
            raise ValueError(f'columns must be at least 6')
        
        if type(self.rows) is not int:
            raise TypeError(f'rows must be int not {type(self.rows)}')

        if self.rows < GameConfig.MIN_ROWS:
            raise ValueError(f'rows must be at least 6')
        
        if type(self.connect_to_win) is not int:
            raise TypeError(f'connect to win must be int not {type(self.connect_to_win)}')

        if self.connect_to_win < GameConfig.MIN_CONNECT:
            raise ValueError(f'connect to win must be greater or equal to 4')

        if type(self.versus_human) is not bool:
            raise TypeError(f'versus human must be bool not {type(self.versus_human)}')
        
        if type(self.points_to_win) is not int:
            raise TypeError(f'points to win must be bool not {type(self.points_to_win)}')
        
        if self.points_to_win < GameConfig.MIN_WINS:
            raise ValueError(f'points to win must be greater or equal to 1') 
        
        if type(self.exclude_directions) is not set:
            raise TypeError(f'excluded directions must be contained in a set') 

        if any(type(direction) for direction in self.exclude_directions) \
            is not Directions:
            raise TypeError(f'excluded directions must only contain Direction objects')



@dataclass(frozen = True)
class GameConfig:
    MIN_ROWS = 6
    MIN_COLS = 6
    MIN_CONNECT = 4
    MIN_WINS = 1