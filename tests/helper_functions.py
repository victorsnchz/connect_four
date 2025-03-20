import sys
sys.path.append('src/')
from bookkeeping import Piece

def save_output(test_case: str, test_name: str, content_to_save: str):
    file_to_write = f'{test_case}/data/results/{test_name}.txt'
    
    with open(file_to_write, 'w') as file:
        file.write(content_to_save)
    
def test_as_filename(test_case: str, test_name: str, folder: str = 'inputs'):
    return f'tests/data/{test_case}/{folder}/{test_name}.txt'

def read_file(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    
    return content

def read_file_as_board(file_name: str):
    
    with open(file_name, 'r') as file:
        board = [[Piece(char) for char in line if char.isalpha()] 
                 for line in file.readlines()]

    return board

def get_numeric_targets(test_case, test_name):
    
    target_file = test_as_filename(test_case=test_case, 
                                    test_name=test_name,
                                    folder='targets')
    
    targets = read_file(target_file)
    int_targets = [int(target) for target in targets.split(', ') 
                   if target.lstrip('-').isnumeric()]

    return int_targets

def get_bool_targets(test_case, test_name):
    
    target_file = test_as_filename(test_case=test_case, 
                                    test_name=test_name,
                                    folder='targets')
    
    targets = read_file(target_file)
    targets = [bool(int(target)) for target in targets 
               if target == '0' or target == '1']

    return targets

def get_board_input(test_case, test_name):
     
    input_file = test_as_filename(test_case=test_case, 
                                    test_name=test_name,
                                    folder='inputs')
     
    board = read_file_as_board(file_name=input_file)

    return board

def get_board_target(test_case, test_name):
     
    target_file = test_as_filename(test_case=test_case, 
                                    test_name=test_name,
                                    folder='targets')
     
    board = read_file_as_board(file_name=target_file)

    return board