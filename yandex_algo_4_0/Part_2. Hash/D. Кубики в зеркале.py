with open("input.txt", "r") as reader:
    N, M = map(int, reader.readline().split(" "))
    toys_lst = [int(n) for n in reader.readline().strip().split(" ")]

P = 10**9 + 7
x_ = 257


def lst_hashing(line_to_check):
    n = len(line_to_check)
    h = [0] * (n + 1)
    x = [0] * (n + 1)

    x[0] = 1
    line_to_check = [" "] + line_to_check

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + int(line_to_check[i])) % P
        x[i] = (x[i - 1] * x_) % P

    return h, x


def is_equal(from_1, from_2, s_len, h, x):
    return ((h[from_1 + s_len - 1] + h[from_2 - 1] * x[s_len]) % P) == (
        (h[from_2 + s_len - 1] + h[from_1 - 1] * x[s_len]) % P
    )


s = toys_lst
concatenated_s = s + s[::-1]
h, x = lst_hashing(concatenated_s)

ans = []

# Perform the comparisons
for n in range(1, len(s) // 2 + 1):
    # The second half reversed starts after the original string in the concatenated string
    second_half_reversed_start = len(s) + len(s) - 2 * n
    second_half_reversed_end = len(s) + len(s) - n

    is_equal_symmetry = is_equal(1, second_half_reversed_start + 1, n, h, x)
    if is_equal_symmetry:
        ans.append(len(s) - n)


ans.append(len(s))
ans.sort()
"""

ans = []
s = toys_lst
reversed_s = s[::-1]
# Perform the comparisons
for n in range(0, len(s) // 2 + 1):  # +1 to include the midpoint
    first_half = s[:n]
    # Correctly extract the reversed substring from the reversed string
    # This will get the equivalent of s[n:2n] reversed
    second_half_reversed = reversed_s[len(s)-2*n:len(s)-n]
    is_equal = first_half == second_half_reversed
    if is_equal:
        ans.append(len(s) - n)

ans.sort()

"""
# Writing to the file
with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
