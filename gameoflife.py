from typing import List
import sys
import os
from time import sleep
import time

clear = lambda: os.system('clear')
 
def get_state_from_file(file_path: str) -> List[List[int]]:
    state = []
    with open(file_path, 'r') as state_file:
        rows = state_file.read().split('\n')
        for row in rows:
            state.append([int(cell) for cell in row.split(', ')])
    return state

def print_state(state: List[List[int]]) -> None:
    for row in state:
        print('|' + ' '.join((' ' if n == 0 else '*' for n in row)) + '|', '\n')

def get_new_cell_state(state: List[List[int]], row: int, cell: int) -> int:
  live_neighbors = sum_of_neighbors(state, row, cell)
  if state[row][cell] == 1 and live_neighbors == 2:
    return 1
  if live_neighbors == 3:
    return 1
  return 0

def sum_of_neighbors(matrix: List[List[int]], row: int, col: int) -> int:
    rows, cols = len(matrix), len(matrix[0])
    total = 0

    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, col-1), min(cols, col+2)):
            if (i, j) != (row, col):
                total += matrix[i][j]

    return total

def game_of_life(state: List[List[bool]]) -> List[List[int]]:
  new_state = [[0 for _ in range(len(row))] for row in state]
  for row, _ in enumerate(state):
    for col, _ in enumerate(state[row]):
        new_state[row][col] = get_new_cell_state(state, row, col)

  return new_state

if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise Exception("Should pass 2 arguments: initital state file path, num of generations")

    initial_state_file_path = sys.argv[1]

    if not sys.argv[2].isdigit():
        raise Exception("Second argument should be a number")
    
    generations_number = int(sys.argv[2])

    initial_state = get_state_from_file(initial_state_file_path)

    cur_state = initial_state
    for i in range(generations_number):
        start = time.time()
        cur_state = game_of_life(cur_state)
        end = time.time()
        sleep(0.1 - end + start ) # Make sure there are at least 100 ml between prints
        clear()
        print_state(cur_state)
        
    
