letters_template = {
    "I": [['#']],
    "O": [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"]],
    "C": [["#", "#"], ["#", "."], ["#", "#"]], 
    "L": [["#", "."], ["#", "#"]],
    "H": [["#", ".", "#"], ["#", "#", "#"], ["#", ".", "#"]],
    "P": [["#", "#", "#"], ["#", ".", "#"], ["#", "#", "#"], ["#", ".", "."]],
}


with open("input.txt", "r") as reader:
    n = int(reader.readline())
    grid = []
    for row in range(n):
        chars = [char for char in reader.readline().strip()]
        grid.append(chars)

def print_grid(grid):
    # Print the grid
    for row in grid:
        print(" ".join(row))

def cut_all_empty_rows(grid):
    for i in range(len(grid)):
        if any([char != "." for char in grid[i]]):
            break
        if all([char == "." for char in grid[i]]):
            grid.pop(i)
            return cut_all_empty_rows(grid)
    for i in range(len(grid) - 1, -1, -1):
        if any([char != "." for char in grid[i]]):
            break
        if all([char == "." for char in grid[i]]):
            grid.pop(i)
            return cut_all_empty_rows(grid)
    return grid

def cut_all_empty_columns(grid):
    for i in range(len(grid[0])):
        if any([row[i] != "." for row in grid]):
            break
        if all([row[i] == "." for row in grid]):
            for row in grid:
                row.pop(i)
            return cut_all_empty_columns(grid)
    for i in range(len(grid[0]) - 1, -1, -1):
        if any([row[i] != "." for row in grid]):
            break
        if all([row[i] == "." for row in grid]):
            for row in grid:
                row.pop(i)
            return cut_all_empty_columns(grid)
    return grid

def cut_same_rows(grid):
    for i in range(len(grid) - 1):
        if grid[i] == grid[i + 1]:
            grid.pop(i)
            return cut_same_rows(grid)
    return grid

def cut_same_cols(grid):
    for i in range(len(grid[0]) - 1):
        if all([row[i] == row[i + 1] for row in grid]):
            for row in grid:
                row.pop(i)
            return cut_same_cols(grid)
    return grid

def compare_to_letter_template(grid, letters_template):
    """
    Compare grid to letter template

    return letter if grid is equal to letter template
    """
    for letter, template in letters_template.items():
        if grid == template:
            return letter
    return None


#cut all empty rows
grid = cut_all_empty_rows(grid)
#cut all empty columns
if grid:
    grid = cut_all_empty_columns(grid)
    #cut same rows
    grid = cut_same_rows(grid)
    #cut same columns
    grid = cut_same_cols(grid)
    #compare to letter template
    letter = compare_to_letter_template(grid, letters_template)
else:
    letter = None

if letter:
    ans = letter
else:
    ans = "X"

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
