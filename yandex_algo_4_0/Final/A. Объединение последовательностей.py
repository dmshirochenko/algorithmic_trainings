#!/usr/bin/env python3
import math


with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())


def merging_lists(n):
    merged_list = []
    square_index, cube_index = 0, 0
    square, cube = 0, 0

    while square_index < n or cube_index < n:
        if cube_index == n or (square_index < n and square <= cube):
            if merged_list and merged_list[-1] == square:
                pass
            else:
                merged_list.append(square)
            square_index += 1
            square = square_index * square_index
        else:
            if merged_list and merged_list[-1] == cube:
                pass
            else:
                merged_list.append(cube)
            cube_index += 1
            cube = cube_index * cube_index * cube_index

        if len(merged_list) == n + 1:
            break
    return merged_list

    return merged_list


if N == 1:
    ans = [0, 1]
elif N == 2:
    ans = [0, 1, 4]
else:
    ans = merging_lists(N)

    print(ans)
with open("output.txt", "w") as file:
    file.write(str(ans[N]))

# [0, 1, 4, 8, 9, 27]
