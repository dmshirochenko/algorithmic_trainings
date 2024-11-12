with open("input.txt", "r") as reader:
    initial_equasion_to_solve = reader.readline().strip()

operations_priority = {
    "+": 0,
    "-": 0,
    "*": 1,
}

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
}

brakets_map = {"(": ")"}


def check_if_brackets_are_correct(brackets_to_check):
    stack = []

    for bracket in brackets_to_check:
        if bracket in brakets_map:
            stack.append(bracket)
        else:
            if bracket != ")":
                continue
            if not stack:
                return False
            last_bracket = stack.pop()
            if brakets_map[last_bracket] != bracket:
                return False

    return not stack and True


#print("equasion_to_solve=", equasion_to_solve)
#equasion_to_solve= 1+(2*2 - 3)
def check_for_valid_brackets(current_char, last_valid_char):
    #wrong case 1*2*3+(*4*5*6*7+8*9)
    if last_valid_char:
        if current_char == "(" and last_valid_char == "digit":
            return False
        if current_char == ")" and last_valid_char == "operation":
            return False
        if current_char == "(" and last_valid_char == ")":
            return False
        if current_char == ")" and last_valid_char == "(":
            return False
        if current_char in "+-*/" and last_valid_char == "(":
            return False
    return True


def replace_substract_sign_before_number(equasion):
    if equasion[0] == "-":
        equasion = "0" + equasion
    #replace (- with (0-
    for i in range(1, len(equasion)):
        if equasion[i] == "-" and equasion[i - 1] == "(":
            equasion = equasion[:i] + "0" + equasion[i:]
    
    return equasion

def from_infix_to_postfix(equasion):
    stack = []
    postfix = []
    is_equasion_valid = True
    left_index = 0
    last_valid_char = None
    while left_index < len(equasion):
        if not check_for_valid_brackets(equasion[left_index], last_valid_char):
            is_equasion_valid = False
            break
        if equasion[left_index] not in operations_priority and equasion[left_index] not in "1234567890() ":
            is_equasion_valid = False
            break
        elif equasion[left_index] == " ":
            left_index += 1
            continue
        elif equasion[left_index].isdigit():
            # check if next element is digit too
            right_index = left_index + 1
            while right_index < len(equasion) and equasion[right_index].isdigit():
                right_index += 1
            postfix.append(equasion[left_index:right_index])
            left_index = right_index - 1

            # check if next element is not digit
            while right_index < len(equasion) and equasion[right_index] == " ":
                right_index += 1
            
            if right_index < len(equasion) and (equasion[right_index] not in "+-*)" or last_valid_char == "digit"):
                is_equasion_valid = False
                break
            
            last_valid_char = "digit"

        elif equasion[left_index] in operations_priority:
            while stack and stack[-1] in operations_priority and operations_priority[stack[-1]] >= operations_priority[equasion[left_index]]:
                postfix.append(stack.pop())
            stack.append(equasion[left_index])
            
            last_valid_char = "operation"

        elif equasion[left_index] == "(":
            stack.append(equasion[left_index])
            last_valid_char = "("

        elif equasion[left_index] == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            if not stack:
                is_equasion_valid = False
                break
            stack.pop()
            last_valid_char = ")"

        left_index += 1

    if not is_equasion_valid:
        return "WRONG"

    while stack:
        postfix.append(stack.pop())

    return postfix

def cal_for_given_equasion(equasion):
    stack = []
    for char in equasion:
        if char.isdigit():
            stack.append(int(char))
        else:
            if len(stack) < 2:
                return False
            operation = operations[char]
            y = stack.pop()
            x = stack.pop()
            stack.append(operation(x, y))

    return stack[0]


#check if brackets are correct
if not check_if_brackets_are_correct(initial_equasion_to_solve):
    ans = "WRONG"
else:
    equasion_to_solve = replace_substract_sign_before_number(initial_equasion_to_solve)
    postfix_equasion = from_infix_to_postfix(equasion_to_solve)
    if postfix_equasion == "WRONG":
        ans = "WRONG"
    else:
        ans = cal_for_given_equasion(postfix_equasion)
        if ans is False:
            ans = "WRONG"
    #print("ans=", ans)

with open("output.txt", "w") as file:
    file.write(str(ans))