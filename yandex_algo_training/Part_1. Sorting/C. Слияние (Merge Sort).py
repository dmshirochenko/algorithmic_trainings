#!/usr/bin/env python3
import math


with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    if N != 0:
        arr_1 = [int(n) for n in reader.readline().split(" ")]
    else:
        empty_line = reader.readline()
        arr_1 = []

    M = int(reader.readline().strip())

    if M != 0:
        arr_2 = [int(n) for n in reader.readline().split(" ")]
    else:
        empty_line = reader.readline()
        arr_2 = []


def merging_lists(left, right):
    inf_number = math.inf
    left.append(inf_number)
    right.append(inf_number)

    merged_list = []
    left_index, right_index = 0, 0

    while True:
        if (left[left_index] == math.inf) and (right[right_index] == math.inf):
            break
        # choose the smalles element from both lists
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    return merged_list


ans = merging_lists(arr_1, arr_2)


with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
