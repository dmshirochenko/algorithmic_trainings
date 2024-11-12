with open("input.txt", "r") as reader:
    n = int(reader.readline())
    nums = []
    for i in range(n):
        nums.append(reader.readline().strip())

def stack_with_sum(nums):
    ans = []
    stack = []
    for num in nums:
        if num[0] == "+":
            if not stack:
                stack.append((int(num[1:]), int(num[1:])))
            else:
                stack.append((int(num[1:]), stack[-1][1] + int(num[1:])))            
        elif num[0] == "-":
            ans.append(stack.pop()[0])
        elif num[0] == "?":
            k_elements = int(num[1:])

            if k_elements == len(stack):
                ans.append(stack[-1][1])
            else:
                ans.append(stack[-1][1] - stack[-1 - k_elements][1])

    return ans

ans = stack_with_sum(nums)

with open("output.txt", "w") as file:
    for i in ans[:-1]:
        file.write(str(i) + "\n")
    file.write(str(ans[-1]))