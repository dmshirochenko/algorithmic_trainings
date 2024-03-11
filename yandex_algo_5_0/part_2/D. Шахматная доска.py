with open("input.txt", "r") as reader:
    chess_board = [[0 for _ in range(66)] for _ in range(66)]
    N = int(reader.readline().strip())
    for _ in range(N):
        row, col = map(int, reader.readline().strip().split(" "))
        chess_board[row][col] = "X"

MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1)]

perimeter = 0

for row in range(len(chess_board)):
    for col in range(len(chess_board[0])):
        if chess_board[row][col] == "X":
            for row_d, col_d in MOVES:
                new_row, new_col = row + row_d, col + col_d
                if chess_board[new_row][new_col] == 0:
                    perimeter += 1

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(perimeter))
