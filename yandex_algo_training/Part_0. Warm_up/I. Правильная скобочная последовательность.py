# Reading from the file
with open("input.txt", "r") as reader:
    brackets_sequence = reader.readline().strip()

brackets = {"(": ")", "[": "]", "{": "}"}
brackets_stack = []
ans = "yes"


for bracket in brackets_sequence:
    if bracket in brackets:
        brackets_stack.append(bracket)
    elif bracket in brackets.values():
        if not brackets_stack or brackets[brackets_stack.pop()] != bracket:
            ans = "no"
            break

if brackets_stack:
    ans = "no"


# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
