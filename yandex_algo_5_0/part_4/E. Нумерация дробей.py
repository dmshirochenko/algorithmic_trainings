with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())


def find_diagonal_linear(n):
    k = 0
    while (k * (k + 1)) // 2 < n:
        k += 1

    return k


def find_diagonal_binary(n):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if (mid * (mid + 1)) // 2 < n:
            left = mid + 1
        else:
            right = mid

    return left


def find_nth_rational(n, k):
    element_position = n - (k * (k - 1)) // 2 - 1

    if k % 2 == 0:
        numerator = k - element_position
        denominator = element_position + 1
    else:
        numerator = element_position + 1
        denominator = k - element_position

    return numerator, denominator


# diagonal_linear = find_diagonal_linear(N)
diagonal_binary = find_diagonal_binary(N)
numerator, denominator = find_nth_rational(N, diagonal_binary)
ans = f"{numerator}/{denominator}"

with open("output.txt", "w") as file:
    file.write(str(ans))
