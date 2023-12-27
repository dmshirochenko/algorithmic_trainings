with open("input.txt", "r") as reader:
    solved_group_1 = int(reader.readline())
    solved_group_2 = int(reader.readline())
    num_of_tasks = int(reader.readline())


max_group_1 = solved_group_1

if solved_group_2 % num_of_tasks == 0:
    min_group_2 = int(solved_group_2 / num_of_tasks)
else:
    min_group_2 = int((solved_group_2 // num_of_tasks) + 1)


# print(max_group_1, min_group_2)
if max_group_1 > min_group_2:
    ans = "Yes"
else:
    ans = "No"

with open("output.txt", "w") as file:
    file.write(str(ans))
