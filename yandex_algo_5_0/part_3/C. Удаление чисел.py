import math

with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    digit_lst = [int(num) for num in reader.readline().strip().split(" ")]

hash_map = dict()

for digit in digit_lst:
    if digit not in hash_map:
        hash_map[digit] = 1
    else:
        hash_map[digit] += 1

min_element_to_delete = math.inf

for digit, digit_count in hash_map.items():
    curr_num = digit_count
    if (digit + 1) in hash_map:
        curr_one_num = hash_map[digit + 1]
    else:
        curr_one_num = 0

    elements_to_remove = len(digit_lst) - curr_num - curr_one_num

    min_element_to_delete = min(min_element_to_delete, elements_to_remove)


with open("output.txt", "w") as file:
    file.write(str(min_element_to_delete))
