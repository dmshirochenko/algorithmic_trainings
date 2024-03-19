with open("input.txt", "r") as reader:
    m, n = map(int, reader.readline().strip().split(" "))
    grid = []
    for row in range(m):
        chars = [char for char in reader.readline().strip()]
        grid.append(chars)

def print_grid(grid):
    # Print the grid
    for row in grid:
        print(' '.join(row))

def adjust_rectangle(grid, top, left, initial_bottom, initial_right):
    for bottom in range(initial_bottom, top, -1):
        for right in range(initial_right, left, -1):
            valid = True
            for r in range(top, bottom):
                for c in range(left, right):
                    if grid[r][c] != "#":
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return True, bottom, right

    return False, initial_bottom, initial_right

def draw_rectangle(grid, row, col):
    rectangle_size = 0

    right = col
    while right < len(grid[0]) and grid[row][right] == "#":
        right += 1

    bottom = row
    while bottom < len(grid) and grid[bottom][col] == "#":
        bottom += 1

    valid, adjusted_bottom, adjusted_right = adjust_rectangle(grid, row, col, bottom, right)
    if valid:
        for r in range(row, adjusted_bottom):
            for c in range(col, adjusted_right):
                rectangle_size += 1
                grid[r][c] = "b"

    return (rectangle_size, row, col, adjusted_bottom, adjusted_right)

def process_grid(grid):
    rectangles = []

    m, n = len(grid), len(grid[0]) if grid else 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "#":
                rectangle = draw_rectangle(grid, row, col)
                rectangles.append(rectangle)
    
    return rectangles

def draw_second_rectangle(grid, row, col, adjusted_bottom, adjusted_right):
    if abs(row - adjusted_right) > 0:
        bottom = row
        while bottom < len(grid) and grid[bottom][col] == "b":
            bottom += 1
    else:
        bottom = row + 1
    
    for r in range(row, bottom):
        grid[r][col] = "a"

def check_num_of_separate_rectangeles(rectangles):
    if len(rectangles) == 0:
        return False
    if len(rectangles) > 2:
        return False
    elif len(rectangles) == 2:
        return True
    elif len(rectangles) == 1 and rectangles[0][0] == 1:
        return False
    elif len(rectangles) == 1:
        size, row, col, adjusted_bottom, adjusted_right  = rectangles[0]
        draw_second_rectangle(grid, row, col, adjusted_bottom, adjusted_right)
        return True

rectangles = process_grid(grid)
result = check_num_of_separate_rectangeles(rectangles)
if result:
    ans = 'YES' + '\n'
    grid_str = '\n'.join("".join(row) for row in grid)
else:
    ans = 'NO'

# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
    if result:
        file.write(grid_str)