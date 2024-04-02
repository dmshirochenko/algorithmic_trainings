with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    grid = [["*"] * n for _ in range(n)]
    ships_coord = []
    for i in range(n):
        row, col = map(int, reader.readline().strip().split(" "))
        grid[row - 1][col - 1] = "s"
        ships_coord.append((row - 1, col - 1))


def print_grid(grid):
    # Print the grid
    for row in grid:
        print(" ".join(row))


total_num_of_steps = 0

# horizontal sorting
ships_sorted_by_rows = sorted(ships_coord, key=lambda x: x[0], reverse=True)
horiz_level_to_check = 0
for _ in range(n):
    ship_row, ship_col = ships_sorted_by_rows.pop()
    total_num_of_steps += abs(horiz_level_to_check - ship_row)
    grid[ship_row][ship_col] = "*"
    grid[horiz_level_to_check][ship_col] = "s"
    horiz_level_to_check += 1


total_num_of_steps_lst = []
# vertica sorting
for checked_col in range(n):
    total_num_of_steps_per_col = total_num_of_steps
    for ship_row, ship_col in ships_coord:
        if ship_col == checked_col:
            continue
        total_num_of_steps_per_col += abs(checked_col - ship_col)

    total_num_of_steps_lst.append(total_num_of_steps_per_col)


# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(min(total_num_of_steps_lst)))
