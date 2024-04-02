# Чтение из файла
with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    line_to_check = reader.readline().strip()

P = 10**9 + 7
x_ = 257


def lst_hashing(line_to_check):
    n = len(line_to_check)
    h = [0] * (n + 1)
    x = [0] * (n + 1)

    x[0] = 1
    line_to_check = " " + line_to_check

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(line_to_check[i])) % P
        x[i] = (x[i - 1] * x_) % P

    return h, x


def is_equal(from_1, from_2, s_len, h, x):
    return ((h[from_1 + s_len - 1] + h[from_2 - 1] * x[s_len]) % P) == (
        (h[from_2 + s_len - 1] + h[from_1 - 1] * x[s_len]) % P
    )


def binary_search_for_accepted_len(low, high, i, is_equal_func, h, x):
    while low <= high:
        mid = (low + high) // 2
        try:
            if is_equal_func(1, i, mid, h, x):
                low = mid + 1
            else:
                high = mid - 1
        except:
            high = mid - 1
    return high


extended_line = line_to_check + line_to_check[::-1]
h, x = lst_hashing(extended_line)
ans = []

for i in range(n):
    len_to_check = i + 1
    start_index_invert = 2 * n - 1 - i
    accepted_len = binary_search_for_accepted_len(1, len_to_check, start_index_invert + 1, is_equal, h, x)
    ans.append(accepted_len)


# Writing to the file
with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
