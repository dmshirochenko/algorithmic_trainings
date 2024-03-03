# Reading from the file
with open("input.txt", "r") as reader:
    N = reader.readline().strip()
    nums = [int(num) for num in reader.readline().strip().split(' ')]
ans = []

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

prev_result = nums[0]
for i in range(1, len(nums)):
    if is_odd(prev_result) and is_odd(nums[i]):
        # Odd * Odd = Odd
        ans.append('x')
        prev_result *= 3
    elif not is_odd(nums[i]) and is_odd(prev_result):
        # Odd + Even = Odd
        ans.append('+')
        prev_result += 2
    elif not is_odd(prev_result) and not is_odd(nums[i]):
        # Even + Even = Even
        ans.append('+')
        prev_result += 2
    elif not is_odd(prev_result) and is_odd(nums[i]):
        # Even + Odd = Odd
        ans.append('+')
        prev_result += 3

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(''.join(ans)))