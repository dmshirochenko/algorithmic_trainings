# Reading from the file
with open("input.txt", "r") as reader:
    line_to_check = reader.readline().strip()

n = len(line_to_check)
P = 10**9 + 7
x_ = 257

h = [0] * (n + 1)
x = [0] * (n + 1)

x[0] = 1
line_to_check = " " + line_to_check

for i in range(1, n + 1):
    h[i] = (h[i - 1] * x_ + ord(line_to_check[i])) % P
    x[i] = (x[i - 1] * x_) % P


def is_equal(from_1, from_2, s_len):
    return ((h[from_1 + s_len - 1] + h[from_2 - 1] * x[s_len]) % P) == (
        (h[from_2 + s_len - 1] + h[from_1 - 1] * x[s_len]) % P
    )


ans = len(line_to_check) - 1

# print(h)
# print(x)
# "bcabcab"
left = 1
right = 2
len_to_check = len(line_to_check)
shift = 0
while right < len(line_to_check):
    # print("Prefix = " , line_to_check[left:len_to_check - 1])
    # print("Sufix = ", line_to_check[right:len_to_check + shift])
    # print(left, right, len_to_check - 2, shift)
    check_is_equal = is_equal(left, right, len_to_check - 2)
    if check_is_equal:
        ans = right - left
        break

    # print(check_is_equal)
    right += 1
    shift += 1
    len_to_check -= 1

# print('ans =', ans)
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
