# import time

with open("input.txt", "r") as reader:
    n, m = map(int, reader.readline().strip().split(" "))
    grid = []
    for _ in range(n):
        grid.append(list(reader.readline().strip()))


def print_grid(grid):
    for row in grid:
        print(row)


def build_prefix_sum_rectangle(matrix):
    n, m = len(matrix), len(matrix[0])
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = (
                prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1] + (matrix[i - 1][j - 1] == "#")
            )
    return prefix_sum


def build_prefix_sum_left_to_right(matrix):
    n, m = len(matrix), len(matrix[0])
    prefix_sum_left_to_right = [[0] * (m + 1) for _ in range(n)]

    for i in range(n):
        for j in range(1, m + 1):
            prefix_sum_left_to_right[i][j] = prefix_sum_left_to_right[i][j - 1] + (matrix[i][j - 1] == "#")

    return prefix_sum_left_to_right


def check_center_element(matrix, i, j, k, prefix_sum_rectangle):
    if is_center_possible_with_prefix(matrix, i, j, k, prefix_sum_rectangle):
        return True
    return False


def is_center_possible_with_prefix(matrix, i, j, k, prefix_sum):
    n, m = len(matrix), len(matrix[0])
    offset = 0 if k % 2 != 0 else 1

    start_i = i - k // 2 + offset
    end_i = i + k // 2
    start_j = j - k // 2 + offset
    end_j = j + k // 2

    if start_i < 0 or start_j < 0 or end_i >= n or end_j >= m:
        return False

    # Вычисляем количество символов '#' в квадрате с помощью префиксной суммы
    total = (
        prefix_sum[end_i + 1][end_j + 1]
        - prefix_sum[start_i][end_j + 1]
        - prefix_sum[end_i + 1][start_j]
        + prefix_sum[start_i][start_j]
    )

    # Если общее количество '#' равно площади квадрата, то весь квадрат заполнен '#'
    return total == k * k


def check_all_arms(matrix, center_i, center_j, k, prefix_sum_rectangle):
    # Устанавливаем начальные точки для каждой "руки" на расстоянии k от центра
    starts = [
        (center_i - k, center_j),  # Вверх
        (center_i + k, center_j),  # Вниз
        (center_i, center_j - k),  # Влево
        (center_i, center_j + k),  # Вправо
    ]

    for start_i, start_j in starts:
        if not is_center_possible_with_prefix(matrix, start_i, start_j, k, prefix_sum_rectangle):
            return False
    return True


def find_max_plus_l(matrix, i, j, base_k, prefix_sum_rectangle, largest_expanded_k):
    n, m = len(matrix), len(matrix[0])
    low, high = 0, base_k

    while low < high:
        mid = (low + high) // 2
        if check_center_element(matrix, i, j, mid, prefix_sum_rectangle) and check_all_arms(
            matrix, i, j, mid, prefix_sum_rectangle
        ):
            low = mid + 1
        else:
            high = mid
            if high <= largest_expanded_k:
                return largest_expanded_k

    return low - 1


def compute_prefix_sums_n(matrix):
    n, m = len(matrix), len(matrix[0])
    left = [[0] * m for _ in range(n)]
    up = [[0] * m for _ in range(n)]

    # Заполняем префиксные суммы для всех направлений
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "#":
                left[i][j] = (left[i][j - 1] if j > 0 else 0) + 1
                up[i][j] = (up[i - 1][j] if i > 0 else 0) + 1

    return left, up


def find_largest_expanded_plus(matrix, prefix_sum_rectangle):
    n, m = len(matrix), len(matrix[0])
    largest_expanded_k = 0
    count_checked_dots = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != "#":
                continue
            if min(n - i, i + 1, m - j, j + 1) <= largest_expanded_k:
                continue
            if not is_center_possible_with_prefix(matrix, i, j, largest_expanded_k, prefix_sum_rectangle):
                continue
            base_k = min(n - i, i + 1, m - j, j + 1)
            if base_k <= largest_expanded_k:
                continue
            count_checked_dots += 1
            expanded_k = find_max_plus_l(matrix, i, j, base_k, prefix_sum_rectangle, largest_expanded_k)
            largest_expanded_k = max(largest_expanded_k, expanded_k)

    return largest_expanded_k


prefix_sum_rectangle = build_prefix_sum_rectangle(grid)

# start_time = time.time()
ans = find_largest_expanded_plus(grid, prefix_sum_rectangle)
# end_time = time.time()

# print("Время выполнения: {:.2f} секунд".format(end_time - start_time))
with open("output.txt", "w") as file:
    file.write(str(ans))
