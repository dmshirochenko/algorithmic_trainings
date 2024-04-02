import math

with open("input.txt", "r") as reader:
    n, m = map(int, reader.readline().strip().split(" "))
    chars_grid = []
    max_element = (-math.inf, None, None)
    max_element_lst = []
    for row in range(n):
        chars_strength = [int(num) for num in reader.readline().strip().split(" ")]
        for col, char in enumerate(chars_strength):
            if char > max_element[0]:
                max_element = (char, row, col)
                max_element_lst = [max_element]
            elif char == max_element[0]:
                max_element_lst.append((char, row, col))

        chars_grid.append(chars_strength)
# here
max_left_elements_lst = set()
index_to_select = (None, None)

for curr_max_element in max_element_lst:
    el_val, max_element_row, max_element_col = curr_max_element
    # select row(class) as first choice
    for col_to_ban in range(len(chars_grid[0])):
        max_left_element = -math.inf
        for row in range(len(chars_grid)):
            if row == max_element_row:
                continue
            for col in range(len(chars_grid[0])):
                if col == col_to_ban:
                    continue

                if chars_grid[row][col] > max_left_element:
                    max_left_element = chars_grid[row][col]
                    index_to_select = (max_element_row + 1, col_to_ban + 1)

        max_left_elements_lst.add((max_left_element, index_to_select))

    # select col(race) as first choice
    for row_to_ban in range(len(chars_grid)):
        max_left_element = -math.inf
        for row in range(len(chars_grid)):
            if row == row_to_ban:
                continue
            for col in range(len(chars_grid[0])):
                if col == max_element_col:
                    continue

                if chars_grid[row][col] > max_left_element:
                    max_left_element = chars_grid[row][col]
                    index_to_select = (row_to_ban + 1, max_element_col + 1)

        max_left_elements_lst.add((max_left_element, index_to_select))


min_element = math.inf
index_to_select = None

for val, index in max_left_elements_lst:
    if val < min_element:
        min_element = val
        index_to_select = index

ans = " ".join(str(element) for element in index_to_select)
# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
