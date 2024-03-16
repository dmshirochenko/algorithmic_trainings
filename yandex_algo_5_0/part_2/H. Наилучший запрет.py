import math

with open("input.txt", "r") as reader:
    n, m = map(int, reader.readline().strip().split(" "))
    chars_grid = []
    max_element_first_index = (None, None)
    max_element_second_index = (None, None)
    max_element_first = -math.inf
    max_element_second = -math.inf
    for row in range(n):
        chars_strength = [int(num) for num in reader.readline().strip().split(" ")]
        for col, char in enumerate(chars_strength):
            if max_element_first < char:
                max_element_first = char
                max_element_first_index = (row, col)

        chars_grid.append(chars_strength)

for row in range(len(chars_grid)):
    for col in range(len(chars_grid[0])):
        if (
            (max_element_second < chars_grid[row][col])
            and (max_element_first_index[0] != row)
            and (max_element_first_index[1] != col)
        ):
            max_element_second = chars_grid[row][col]
            max_element_second_index = (row, col)

index_to_select = (None, None)
max_left_elements_lst = []
row_first_max, col_first_max = max_element_first_index
row_second_max, col_second_max = max_element_second_index

possible_bans = [(row_first_max, col_first_max), (row_first_max, col_second_max), (row_second_max, col_first_max)]

for row_ban, col_ban in possible_bans:
    max_left_element = -math.inf
    for row in range(len(chars_grid)):
        if row == row_ban:
            continue
        for col in range(len(chars_grid[0])):
            if col == col_ban:
                continue

            if chars_grid[row][col] > max_left_element:
                max_left_element = chars_grid[row][col]
                index_to_select = (row_ban + 1, col_ban + 1)

    max_left_elements_lst.append((max_left_element, index_to_select))

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
