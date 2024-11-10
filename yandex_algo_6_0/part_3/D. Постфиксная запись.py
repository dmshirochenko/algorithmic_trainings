with open("input.txt", "r") as reader:
    equasion = reader.readline().strip().split()

operands = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}


def cal_for_given_equasion(equasion):
    stack = []
    for char in equasion:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand = operands[char]
            y = stack.pop()
            x = stack.pop()
            stack.append(operand(x, y))

    return stack[0]


ans = cal_for_given_equasion(equasion)

with open("output.txt", "w") as file:
    file.write(str(ans))
