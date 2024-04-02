# Reading file
with open("input.txt", "r") as reader:
    students_count = int(reader.readline())
    students = [int(n) for n in reader.readline().split(" ")]

ans = []
sum = 0
# count first element
for i in range(1, len(students)):
    sum += abs(students[i] - students[0])
ans.append(sum)

# count rest elements
for j in range(1, len(students)):
    elements_diff = students[j] - students[j - 1]
    count_elements_from_left = j
    count_elements_from_right = len(students) - j - 1
    element_to_add = (
        ans[j - 1]
        + students[j - 1]
        - students[j]
        + (count_elements_from_left * elements_diff)
        - (count_elements_from_right * elements_diff)
    )
    ans.append(element_to_add)


with open("output.txt", "w") as writer:
    writer.write(" ".join(str(item) for item in ans))
