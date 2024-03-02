from collections import deque

N = 8

BISHOP_MOVES = {
    "UL": (-1, -1),  # Up-Left diagonal
    "UR": (-1, 1),   # Up-Right diagonal
    "DL": (1, -1),   # Down-Left diagonal
    "DR": (1, 1)     # Down-Right diagonal
}

ROOK_MOVES = {
    "U": (-1, 0),  # Up
    "L": (0, -1),  # Left
    "D": (1, 0),   # Down
    "R": (0, 1)    # Right
}

# Reading from the file
with open("input.txt", "r") as reader:
    board_grid = []
    chess_figures = []
    for row in range(N):
        board_line = reader.readline().strip()
        board_lst = []
        for col in range(len(board_line)):
            if board_line[col] == "B":
                chess_figures.append((BISHOP_MOVES, (0, 0), row, col))
            if board_line[col] == "R":
                chess_figures.append((ROOK_MOVES, (0, 0),row, col))
            board_lst.append(board_line[col])
        board_grid.append(board_lst)


def is_within_grid(coordinates, grid):
    x, y = coordinates
    return 0 <= x < len(grid) and 0 <= y < len(grid[0])

non_beaten_cells = N * N - len(chess_figures)

queue = deque()
seen_empty_cells = set()
for figure in chess_figures:
    queue.append(figure)

while queue:
    cell_to_check = queue.popleft()
    moves, direction, row, col = cell_to_check

    if (direction, row, col) in seen_empty_cells:
        continue

    seen_empty_cells.add((direction, row, col))
    
    for move in moves.values():
        new_row, new_col = row + move[0], col + move[1]
        if is_within_grid((new_row, new_col), board_grid):
            cell_symbol = board_grid[new_row][new_col]
            if cell_symbol == '*':
                queue.append(({"CELL": move}, move, new_row, new_col))
                board_grid[new_row][new_col] = 'X'
                non_beaten_cells -= 1
            elif cell_symbol == 'X':
                queue.append(({"CELL": move}, move, new_row, new_col))
     


#for row in board_grid:
#    print(' '.join(row))
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(non_beaten_cells))