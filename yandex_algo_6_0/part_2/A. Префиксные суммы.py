with open('input.txt', 'r') as reader:
    n = int(reader.readline())
    nums = list(map(int, reader.readline().split()))

def prefix_sums(nums):
    prefix_sums = [0]
    for i in range(1, len(nums) + 1):
        prefix_sums.append(prefix_sums[i - 1] + nums[i - 1])
    return prefix_sums

prefix_sums = prefix_sums(nums)
ans = ''
for i in prefix_sums[1:]:
    ans += str(i) + ' '

with open("output.txt", "w") as file:
    file.write(ans)