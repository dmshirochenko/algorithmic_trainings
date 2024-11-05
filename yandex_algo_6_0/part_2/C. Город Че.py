with open("input.txt", "r") as reader:
    n, r = map(int, reader.readline().split())
    nums = list(map(int, reader.readline().split()))

# print("nums=", nums)
right = 1
possible_combinations = 0

for left in range(n):
    if left == right:
        right += 1
    # print("nums[right]=", nums[right], "nums[left]=", nums[left])
    while right < n and nums[right] - nums[left] <= r:
        right += 1

    possible_combinations += len(nums) - right

# print("possible_combinations=", possible_combinations)

with open("output.txt", "w") as file:
    file.write(str(possible_combinations))
