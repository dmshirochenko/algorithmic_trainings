# Reading from the file
with open("input.txt", "r") as reader:
    line_to_check = reader.readline().strip()
    N = int(reader.readline())
    indexes_to_check = []
    for i in range(N):
        arr_to_add = [int(n) for n in reader.readline().split(" ")]
        indexes_to_check.append(arr_to_add)

ans = []

for l, left_1, left_2 in indexes_to_check:
    is_equal = True
    for i in range(l):
        if line_to_check[left_1 + i] != line_to_check[left_2 + i]:
            is_equal = False
            break
    if is_equal:
        ans.append("yes")
    else:
        ans.append("no")

# Writing to the file
with open("output.txt", "w") as file:
    for item in ans:
        file.write("%s\n" % item)
