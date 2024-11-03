import math

with open("input.txt", "r") as reader:
    n = int(reader.readline())
    nums = list(map(int, reader.readline().split()))


def delete_median(nums):
    # sort the list
    nums.sort()
    merged_list = []

    if len(nums) % 2 == 0:
        # split the list into two halves
        first_half = [float("inf")] + nums[: len(nums) // 2]
        second_half = nums[len(nums) // 2 :] + [float("inf")]
    else:
        # split the list into two halves
        first_half = [float("inf")] + nums[: len(nums) // 2 + 1]
        second_half = nums[len(nums) // 2 + 1 :] + [float("inf")]

    left_index = len(first_half) - 1
    right_index = 0

    # print("first_half=", first_half)
    # print("second_half=", second_half)
    while True:
        if (first_half[left_index] == math.inf) and (second_half[right_index] == math.inf):
            break
        # print(len(first_half[:left_index + 1]), len(second_half[right_index:]))
        if len(first_half[: left_index + 1]) > len(second_half[right_index:]):
            # print('left bigger')
            merged_list.append(first_half[left_index])
            left_index -= 1
        elif len(first_half[: left_index + 1]) < len(second_half[right_index:]):
            # print('right bigger')
            merged_list.append(second_half[right_index])
            right_index += 1
        else:
            # print('equal')
            if first_half[left_index] < second_half[right_index]:
                merged_list.append(first_half[left_index])
                left_index -= 1
            else:
                merged_list.append(second_half[right_index])
                right_index += 1

        # print("merged_list=", merged_list)
        # print("left_index=", left_index)
        # print("right_index=", right_index)

    return merged_list


ans = delete_median(nums)


with open("output.txt", "w") as file:
    file.write(" ".join(map(str, ans)))
