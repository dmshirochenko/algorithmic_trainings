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


def binary_search_for_accepted_len(low, high, i, is_equal_func):
    while low <= high:
        mid = (low + high) // 2
        try:
            if is_equal_func(1, i, mid):
                low = mid + 1
            else:
                high = mid - 1
        except:
            high = mid - 1
    return high


# Создание расширенной строки путем конкатенации исходной строки и её инверсии
extended_line = line_to_check + line_to_check[::-1]

ans = [0] * (2 * n)

for i in range(1, n + 1):
    # Вычисляем длину, которую нужно проверить, на расширенной строке
    len_to_check = min(i, 2 * n - i + 1)

    # Вычисляем максимально возможное k для зеркальной z-функции
    accepted_len = binary_search_for_accepted_len(1, len_to_check, i, is_equal)

    ans[i - 1] = accepted_len

# Writing to the file
with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
# Writing to the file
with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
