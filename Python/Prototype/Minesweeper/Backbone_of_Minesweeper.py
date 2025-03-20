import numpy as np
import random as rand

def generate_board(size, difficulty):

    mines = round(difficulty/100 * (size[0]*size[1]))

    mine_placements = set()
    
    board = np.matrix([[0 for j in range(size[0])] for i in range(size[1])], dtype=np.int8)

    while len(mine_placements) < mines:

        row = rand.randint(0, size[1]-1)
        column = rand.randint(0, size[0]-1)

        mine_placements.add((row, column))

    for mine_placement in mine_placements:
        
        surrounding_row = [mine_placement[0]-1, mine_placement[0]+1]
        surrounding_column = [mine_placement[1]-1, mine_placement[1]+1]

        if mine_placement[0] == 0:
            surrounding_row[0] = 0
        if mine_placement[1] == 0:
            surrounding_column[0] = 0
        
        if mine_placement[0] == size[1]-1:
            surrounding_row[1] = size[1]-1
        if mine_placement[1] == size[0]-1:
            surrounding_column[1] = size[0]-1
        
        board[mine_placement[0], mine_placement[1]] = -1

        for r in range(surrounding_row[0], surrounding_row[1]+1):
            for c in range(surrounding_column[0], surrounding_column[1]+1):
                if board[r, c] != -1:
                    board[r, c] += 1

    return board, list(mine_placements)

def check_empty_surrounding(board, reveal, coords):

    size = board.shape[::-1]

    reveal.append(coords)

    surrounding_row = [coords[0]-1, coords[0]+1]
    surrounding_column = [coords[1]-1, coords[1]+1]

    if coords[0] == 0:
        surrounding_row[0] = 0
    if coords[1] == 0:
        surrounding_column[0] = 0
    
    if coords[0] == size[1]-1:
        surrounding_row[1] = size[1]-1
    if coords[1] == size[0]-1:
        surrounding_column[1] = size[0]-1

    for r in range(surrounding_row[0], surrounding_row[1]+1):
        for c in range(surrounding_column[0], surrounding_column[1]+1):
            if (board[r, c] == 0) and ((r, c) not in reveal):
                reveal = check_empty_surrounding(board, reveal, (r, c))
            elif (board[r, c] != 0) and (board[r, c] != -1):
                reveal.append((r, c))

    return reveal

def make_move(board, coords):

    reveal = []

    if board[coords[0], coords[1]] == 0:
        reveal = check_empty_surrounding(board, reveal, coords)
    elif board[coords[0], coords[1]] != -1:
        reveal = [coords]
    else:
        reveal = "Game Over!"

    return reveal

if __name__ == '__main__':
    
    board = generate_board((10, 10), 15)

    reveal = make_move(board, (1, 2))

    print(reveal)
    print(board)