import sys
sys.path.append('tests')
import helper_functions

def main():
    
    grid = helper_functions.read_file_as_grid('tests/data/inputs/test_count_to_three_all_directions.txt')
    print(grid)

if __name__ == '__main__':
    main()