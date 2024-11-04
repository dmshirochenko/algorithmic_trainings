with open("input.txt", "r") as reader:
    n = int(reader.readline())
    nums = list(map(int, reader.readline().split()))

def triple_product(nums):
    prefix_sums = [0]
    for i in range(1, len(nums) + 1):
        prefix_sums.append(prefix_sums[i - 1] + nums[i - 1])

    ans = 0
    for i in range(1, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            ans += nums[i - 1] * nums[j - 1] * (prefix_sums[-1] - prefix_sums[j])

    return ans % 1000000007

ans = triple_product(nums)

with open("output.txt", "w") as file:
    file.write(str(ans))