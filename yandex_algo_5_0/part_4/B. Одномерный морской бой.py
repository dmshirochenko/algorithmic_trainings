with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())


def find_total_num_of_squares(k):
    return ((k * ((k**2) + (6 * k) + 5)) // 6) - 1


def binary_search(left, right, n):
    while left < right:
        mid_index = (left + right + 1) // 2

        if find_total_num_of_squares(mid_index) <= n:
            left = mid_index
        else:
            right = mid_index - 1

    return left


ans = binary_search(1, N, N)

with open("output.txt", "w") as file:
    file.write(str(ans))
