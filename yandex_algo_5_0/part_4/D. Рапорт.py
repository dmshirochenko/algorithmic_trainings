import math

with open("input.txt", "r") as reader:
    w, n, m = map(int, reader.readline().strip().split(" "))
    message_a = [int(num) for num in reader.readline().strip().split(" ")]
    message_b = [int(num) for num in reader.readline().strip().split(" ")]


def num_of_lines_based_on_the_split(message, w):
    num_of_lines = 1
    current_line = 0
    for i in range(len(message)):
        if message[i] > w:
            return math.inf

        if current_line + message[i] + 1 < w:  # add 1 for space
            current_line += message[i] + 1
        elif current_line + message[i] <= w:  # last word in the line
            if len(message) - 1 != i:
                num_of_lines += 1
            current_line = 0
        else:
            num_of_lines += 1
            current_line = message[i] + 1
    return num_of_lines


def binary_search(left, right, message_a, message_b):
    min_lines_to_split = math.inf
    while left < right:
        mid = (left + right) // 2
        lines_a = num_of_lines_based_on_the_split(message_a, mid)
        lines_b = num_of_lines_based_on_the_split(message_b, w - mid - 1)
        if lines_a > lines_b:
            left = mid + 1
        elif lines_a < lines_b:
            right = mid
        else:
            return mid

    return left


# linear search
def linear_search(max_w, message_a, message_b):
    index_for_split = -1
    min_lines_to_split = math.inf
    for i in range(1, max_w):
        lines_a = num_of_lines_based_on_the_split(message_a, i)
        lines_b = num_of_lines_based_on_the_split(message_b, w - i)
        # print('i, lines_a, lines_b', i, lines_a, lines_b)
        if min_lines_to_split > max(lines_a, lines_b):
            min_lines_to_split = max(lines_a, lines_b)
            index_for_split = i

    return index_for_split


index_to_split_linear = linear_search(w, message_a, message_b)
print("index_to_split_linear", index_to_split_linear)
ans_linear = max(
    num_of_lines_based_on_the_split(message_a, index_to_split_linear),
    num_of_lines_based_on_the_split(message_b, w - index_to_split_linear),
)

index_for_split = binary_search(1, w, message_a, message_b)
print("index_for_split", index_for_split)
ans = max(
    num_of_lines_based_on_the_split(message_a, index_for_split),
    num_of_lines_based_on_the_split(message_b, w - index_for_split),
)

print("ans_linear", ans_linear, "ans", ans)
with open("output.txt", "w") as file:
    file.write(str(ans))
