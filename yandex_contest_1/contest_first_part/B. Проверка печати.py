# Reading from the file
with open("input.txt", "r") as reader:
    initial_string = reader.readline().strip() 
    string_with_actions = [str(char) for char in reader.readline().strip()]

def delete_from_line(lst, cursor_position):
    if cursor_position < len(lst):
        del lst[cursor_position]
    return lst, cursor_position

def backspace_from_line(lst, cursor_position):
    if cursor_position > 0:
        del lst[cursor_position - 1]
        cursor_position -= 1
    return lst, cursor_position

def move_cursor_left(lst, cursor_position):
    if cursor_position > 0:
        cursor_position -= 1
    return lst, cursor_position

def move_cursor_right(lst, cursor_position):
    if cursor_position < len(lst):
        cursor_position += 1
    return lst, cursor_position


actions_map = {
    "<delete>" : delete_from_line,
    "<bspace>" : backspace_from_line,
    "<left>" : move_cursor_left,
    "<right>" : move_cursor_right,
}

left_index = 0
cursor_position = 0
action_to_check = ""
final_lst = []
while left_index < len(string_with_actions):
    if string_with_actions[left_index] == "<" and action_to_check == "":
        action_to_check = ""
        while left_index < len(string_with_actions) and string_with_actions[left_index] != ">":
            action_to_check += string_with_actions[left_index]
            left_index += 1
        if left_index < len(string_with_actions):
            action_to_check += string_with_actions[left_index]
        left_index += 1
    else:
        if action_to_check:
            if action_to_check in actions_map:
                final_lst, cursor_position = actions_map[action_to_check](final_lst, cursor_position)
                action_to_check = ""
        else:
            final_lst.insert(cursor_position, string_with_actions[left_index])
            cursor_position += 1
            left_index += 1
else:
    if action_to_check:
        if action_to_check in actions_map:
            final_lst, cursor_position = actions_map[action_to_check](final_lst, cursor_position)
            action_to_check = ""
    

ans = "YES" if initial_string == "".join(final_lst) else "NO"
# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)