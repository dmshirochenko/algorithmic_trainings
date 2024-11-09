with open("input.txt", "r") as reader:
    brackets_to_check = reader.readline().strip()

brakets_map = {
    "(": ")",
    "{": "}",
    "[": "]"
}


def check_if_brackets_are_correct(brackets_to_check):
    stack = []

    for bracket in brackets_to_check:
        if bracket in brakets_map:
            stack.append(bracket)
        else:
            if not stack:
                return "no"
            last_bracket = stack.pop()
            if brakets_map[last_bracket] != bracket:
                return "no"

    return "yes" if not stack else "no"


ans = check_if_brackets_are_correct(brackets_to_check)
with open("output.txt", "w") as file:
    file.write(str(ans))