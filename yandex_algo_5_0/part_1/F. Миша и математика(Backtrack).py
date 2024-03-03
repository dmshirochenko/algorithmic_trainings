import sys

sys.setrecursionlimit(100000)

# Reading from the file
with open("input.txt", "r") as reader:
    N = reader.readline().strip()
    nums = [int(num) for num in reader.readline().strip().split(" ")]

N = len(nums)
answers = []


def get_operations(index, prev_operand, value, string):
    if answers:
        return

    if index == N:
        if value % 2 != 0:
            answers.append("".join(string[1:]))
        return

    current_operand = nums[index]

    # Addition
    string.append("+")
    get_operations(index + 1, current_operand, value + current_operand, string)
    string.pop()

    if string:
        # Multiplication
        string.append("x")
        get_operations(
            index + 1, current_operand * prev_operand, value - prev_operand + (current_operand * prev_operand), string
        )
        string.pop()


get_operations(0, 0, 0, [])
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(answers[0]))
