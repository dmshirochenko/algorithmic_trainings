import math
import random


with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    if N != 0:
        arr_1 = [int(n) for n in reader.readline().split(" ")]
    else:
        arr_1 = []


def quicksort_asc(items_to_sort):
    if len(items_to_sort) <= 1:
        return items_to_sort

    left = []
    equal = []
    right = []

    pivot_element = random.choice(items_to_sort)

    for item in items_to_sort:
        if item < pivot_element:
            left.append(item)
        elif item > pivot_element:
            right.append(item)
        elif item == pivot_element:
            equal.append(item)

    return quicksort_asc(left) + equal + quicksort_asc(right)


if len(arr_1) == 0:
    ans = []
else:
    ans = quicksort_asc(arr_1)

with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
