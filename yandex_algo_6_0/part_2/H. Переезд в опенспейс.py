with open("input.txt", "r") as reader:
    n = map(int, reader.readline().split())
    nums = list(map(int, reader.readline().split()))


def prefix_sums(nums):
    prefix_sums = [0]
    for i in range(1, len(nums) + 1):
        # i need take into account that pesons move n time
        prefix_sums.append(prefix_sums[i - 1] + nums[i - 1])
    return prefix_sums


def suffix_sums(nums):
    suffix_sums = [0]
    for i in range(len(nums) - 1, -1, -1):
        suffix_sums.append(suffix_sums[-1] + nums[i])
    return suffix_sums[::-1]


def min_moves_to_go_to_openspace(nums, prefix_sums, suffix_sums):

    moves_lst = []
    sum_for_first_room = 0
    # count moves_lst[0]
    for i in range(len(nums)):
        sum_for_first_room += nums[i] * i

    moves_lst.append(sum_for_first_room)

    for i in range(1, len(nums)):
        moves_lst.append(moves_lst[i - 1] + prefix_sums[i] - suffix_sums[i])
    return min(moves_lst)


"""
print("nums =", nums)
print("prefix_sums =", prefix_sums)
print("suffix_sums =", suffix_sums)
print("ans =", ans)
"""
if n == 1:
    ans = 0
else:
    prefix_sums = prefix_sums(nums)
    suffix_sums = suffix_sums(nums)
    ans = min_moves_to_go_to_openspace(nums, prefix_sums, suffix_sums)

with open("output.txt", "w") as file:
    file.write(str(ans))
