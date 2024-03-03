# Reading from the file
with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    num_of_spaces_per_line = []
    for i in range(N):
        num_of_spaces_per_line.append(int(reader.readline().strip()))

ans = 0

for space_per_line in num_of_spaces_per_line:
    spaces_left = space_per_line
    # tabs
    num_tabs_possible = spaces_left // 4
    if num_tabs_possible > 0:
        spaces_left = spaces_left % 4
        ans += num_tabs_possible

    # tab + backspaace
    num_backspace_and_one_space = spaces_left // 3
    if num_backspace_and_one_space > 0:
        spaces_left = spaces_left % 3
        ans += num_backspace_and_one_space * 2

    ans += spaces_left

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
