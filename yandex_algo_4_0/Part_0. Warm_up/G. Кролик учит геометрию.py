with open("input.txt", "r") as reader:
    rows, cols = map(int, reader.readline().split(" "))
    grid = []
    for i in range(rows):
        grid.append([int(n) for n in reader.readline().split(" ")])


def find_max_square(matrix, rows, cols):
    max_square_size = 0
    nearest_ones_dp = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                if i == 0 or j == 0:
                    nearest_ones_dp[i][j] = 1
                else:
                    nearest_ones_dp[i][j] = 1 + min(
                        nearest_ones_dp[i - 1][j], nearest_ones_dp[i][j - 1], nearest_ones_dp[i - 1][j - 1]
                    )
                max_square_size = max(max_square_size, nearest_ones_dp[i][j])

    return max_square_size


ans = find_max_square(grid, rows, cols)

with open("output.txt", "w") as file:
    file.write(str(ans))
