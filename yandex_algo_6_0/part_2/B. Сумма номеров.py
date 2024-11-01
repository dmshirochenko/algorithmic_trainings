with open('input.txt', 'r') as reader:
    N, K = map(int, reader.readline().split())
    nums = list(map(int, reader.readline().split()))

def find_length_of_equals_to_k(nums, k):
    left = curr =  0
    times_seen = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        if curr == k:
            times_seen += 1

    return times_seen

ans = find_length_of_equals_to_k(nums, K)

with open("output.txt", "w") as file:
    file.write(str(ans))