with open("input.txt", "r") as reader:
    n = int(reader.readline())
    nums = list(map(int, reader.readline().split()))

def triple_product(nums):
    n = len(nums)
    
    prefix_sum = [0] * n #prefix sum of nums
    prefix_sum[0] = nums[0] 

    #calculate prefix sum and prefix square sum
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i]

    total_sum = 0
    suffix_sum = 0  

    for j in range(n - 2, 0, -1):
        suffix_sum += nums[j + 1]
        
        left_sum = prefix_sum[j - 1]  # Sum of elements before j
        total_sum += nums[j] * (left_sum * suffix_sum)
    
    return total_sum % 1000000007

ans = triple_product(nums)

with open("output.txt", "w") as file:
    file.write(str(ans))