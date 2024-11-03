import math

with open("input.txt", "r") as reader:
    n = int(reader.readline())
    nums = list(map(int, reader.readline().split()))


def delete_median(nums):
    # sort the list
    nums.sort()
    merged_list = []

    left_index = len(nums) // 2 - 1
    right_index = len(nums) // 2
    len_left = len(nums[: left_index + 1])
    len_right = len(nums[right_index:])

    print(nums, nums[: left_index + 1], nums[right_index:], len(nums[: left_index + 1]), len(nums[right_index:]))

    while True:
        if (left_index == -1) and (right_index == len(nums)):
            break
        # print(len(first_half[:left_index + 1]), len(second_half[right_index:]))
        if len_left > len_right:
            # print('left bigger')
            merged_list.append(nums[left_index])
            left_index -= 1
            len_left -= 1
        elif len_left < len_right:
            # print('right bigger')
            merged_list.append(nums[right_index])
            right_index += 1
            len_right -= 1
        else:
            # print('equal')
            if nums[left_index] < nums[right_index]:
                merged_list.append(nums[left_index])
                left_index -= 1
                len_left -= 1
            else:
                merged_list.append(nums[right_index])
                right_index += 1
                len_right -= 1

        # print("merged_list=", merged_list)
        # print("left_index=", left_index)
        # print("right_index=", right_index)

    return merged_list


ans = delete_median(nums)


with open("output.txt", "w") as file:
    file.write(" ".join(map(str, ans)))
