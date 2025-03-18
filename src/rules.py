from dataclasses import dataclass, field

@dataclass(frozen=True)
class Rules:

    columns: int = field(default = 6)
    rows: int = field(default = 6)
    connect_to_win: int =  field(default = 4)
    versus_human: bool = field(default = True)
    points_to_win: int = field(default=1)

    def __post_init__(self):
        self.validate_rules()

    def validate_rules(self):
        
        if type(self.columns) is not int:
            raise TypeError(f'columns must be int not {type(self.columns)}')
        
        if self.columns < 6:
            raise ValueError(f'columns must be at least 6')
        
        if type(self.rows) is not int:
            raise TypeError(f'rows must be int not {type(self.rows)}')

        if self.rows < 6:
            raise ValueError(f'rows must be at least 6')
        
        if type(self.connect_to_win) is not int:
            raise TypeError(f'connect to win must be int not {type(self.connect_to_win)}')

        if self.connect_to_win < 4:
            raise ValueError(f'connect to win must be greater or equal to 4')

        if type(self.versus_human) is not bool:
            raise TypeError(f'versus human must be bool not {type(self.versus_human)}')
        
        if type(self.points_to_win) is not int:
            raise TypeError(f'points to win must be bool not {type(self.points_to_win)}')