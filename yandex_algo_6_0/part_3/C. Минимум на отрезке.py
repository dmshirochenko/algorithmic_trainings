from collections import deque


with open("input.txt", "r") as reader:
    n, k = map(int, reader.readline().split())
    nums = list(map(int, reader.readline().split()))


def min_in_k_interval(nums, k):
    ans = []
    left = 0
    queue = deque()

    for right in range(len(nums)):

        while queue and queue[-1] > nums[right]:
            queue.pop()
        queue.append(nums[right])

        if right - left + 1 > k:
            if queue and nums[left] == queue[0]:
                queue.popleft()
            left += 1

        if right - left + 1 == k:
            ans.append(queue[0])

    return ans


ans = min_in_k_interval(nums, k)

with open("output.txt", "w") as file:
    for i in ans[:-1]:
        file.write(str(i) + "\n")
    file.write(str(ans[-1]))
