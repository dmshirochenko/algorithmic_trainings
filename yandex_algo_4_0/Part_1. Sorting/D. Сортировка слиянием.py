import math


with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    if N != 0:
        arr_1 = [int(n) for n in reader.readline().split(" ")]
    else:
        empty_line = reader.readline()
        arr_1 = []


def merging_lists(left, right):
    inf_number = math.inf
    left.append(inf_number)
    right.append(inf_number)

    merged_list = []
    left_index, right_index = 0, 0

    while True:
        # quit when both left and right lists will hit added before inf number
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


def merge_sort_asc(items_to_sort):
    if len(items_to_sort) <= 1:
        return items_to_sort
    index_to_split = len(items_to_sort) // 2
    left_side = items_to_sort[:index_to_split]
    right_side = items_to_sort[index_to_split:]
    return merging_lists(merge_sort_asc(left_side), merge_sort_asc(right_side))


ans = merge_sort_asc(arr_1)


with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
