with open("input.txt", "r") as reader:
    m, n = map(int, reader.readline().strip().split(" "))
    grid = []
    for row in range(m):
        chars = [char for char in reader.readline().strip()]
        grid.append(chars)


def print_grid(grid):
    # Print the grid
    for row in grid:
        print(" ".join(row))


def adjust_rectangle(grid, top, left, initial_bottom, initial_right):
    for bottom in range(initial_bottom, top, -1):
        for right in range(initial_right, left, -1):
            valid = True
            for r in range(top, bottom):
                for c in range(left, right):
                    if grid[r][c] not in ("a", "#", "b"):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return True, bottom, right

    return False, initial_bottom, initial_right


def adjust_rectangle_right_over_bottom(grid, top, left, initial_bottom, initial_right):
    for right in range(initial_right, left, -1):
        for bottom in range(initial_bottom, top, -1):
            valid = True
            for r in range(top, bottom):
                for c in range(left, right):
                    if grid[r][c] not in ("a", "#", "b"):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                return True, bottom, right

    return False, initial_bottom, initial_right


def draw_rectangle(grid, row, col, char_to_draw, dirrection_priority):
    rectangle_size = 0
    right = col
    is_intersect_b_valid = True
    while right < len(grid[0]) and grid[row][right] in ("a", "#", "b"):
        if grid[row][right] == "b":
            element_from_top = get_element_value(grid, row - 1, right)
            element_from_down = get_element_value(grid, row + 1, right)
            if element_from_top == "b" and element_from_down == "b":
                break
        right += 1

    bottom = row
    while bottom < len(grid) and grid[bottom][col] in ("a", "#", "b"):
        if grid[bottom][col] == "b":
            element_from_left = get_element_value(grid, bottom, col - 1)
            element_from_down = get_element_value(grid, bottom, col + 1)
            if element_from_left == "b" and element_from_down == "b":
                break
        bottom += 1

    if dirrection_priority == "bottom":
        valid, adjusted_bottom, adjusted_right = adjust_rectangle(grid, row, col, bottom, right)
    else:
        valid, adjusted_bottom, adjusted_right = adjust_rectangle_right_over_bottom(grid, row, col, bottom, right)

    if valid:
        for r in range(row, adjusted_bottom):
            for c in range(col, adjusted_right):
                rectangle_size += 1
                grid[r][c] = char_to_draw

    return (rectangle_size, row, col, adjusted_bottom, adjusted_right, char_to_draw)


def process_grid(grid, dirrection_priority):
    rectangles = []
    need_to_rescan = False
    m, n = len(grid), len(grid[0]) if grid else 0
    for row in range(m):
        for col in range(n):
            if grid[row][col] == "#":
                if len(rectangles) == 0:
                    char_to_draw = "b"
                else:
                    char_to_draw = "a"
                rectangle = draw_rectangle(grid, row, col, char_to_draw, dirrection_priority)
                rectangles.append(rectangle)

    return rectangles


def draw_second_rectangle(grid, row, col, adjusted_bottom, adjusted_right):
    if abs(col - adjusted_right) > 1:
        bottom = row
        while bottom < len(grid) and grid[bottom][col] == "b":
            bottom += 1
    else:
        bottom = row + 1

    for r in range(row, bottom):
        grid[r][col] = "a"


def check_num_of_separate_rectangeles(grid, rectangles):
    if len(rectangles) == 0:
        return False
    if len(rectangles) > 2:
        return False
    elif len(rectangles) == 2:
        return True
    elif len(rectangles) == 1 and rectangles[0][0] == 1:
        return False
    elif len(rectangles) == 1:
        size, row, col, adjusted_bottom, adjusted_right, char_to_draw = rectangles[0]
        draw_second_rectangle(grid, row, col, adjusted_bottom, adjusted_right)
        return True


def get_element_value(grid, row, col):
    if 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        return grid[row][col]
    else:
        return None


# direction bottom priority
grid_bottom_priority = [row[:] for row in grid]
rectangles = process_grid(grid_bottom_priority, "bottom")
result = check_num_of_separate_rectangeles(grid_bottom_priority, rectangles)

right_priority = False
if not result:
    # direction right priority
    grid_right_priority = [row[:] for row in grid]
    rectangles = process_grid(grid_right_priority, "right")
    result = check_num_of_separate_rectangeles(grid_right_priority, rectangles)
    right_priority = True

if result:
    ans = "YES" + "\n"
    if right_priority:
        grid_str = "\n".join("".join(row) for row in grid_right_priority)
    else:
        grid_str = "\n".join("".join(row) for row in grid_bottom_priority)
else:
    ans = "NO"

# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
    if result:
        file.write(grid_str)
