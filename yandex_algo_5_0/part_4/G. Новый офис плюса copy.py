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
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + (matrix[i-1][j-1] == '#')
    return prefix_sum

def get_prefix_sum(prefix_sum, x1, y1, x2, y2):
    # Получить сумму в прямоугольнике от (x1, y1) до (x2, y2), включая границы.
    return prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]

def calculate_max_possible_plus_size(prefix_sum, i, j, n, m, current_largest_k):
    max_possible_k = 1  # Начинаем с минимально возможного "плюса"

    for k in range(1, min(n, m) // 2 + 1):
        # Проверка, что "плюс" размером k уместится в матрицу
        if i - k < 0 or i + k >= n or j - k < 0 or j + k >= m:
            break

        # Проверяем вертикальную и горизонтальную линии "плюса"
        vertical_sum = get_prefix_sum(prefix_sum, i-k+1, j, i+k, j)  # Сумма символов '#' в вертикальной линии
        horizontal_sum = get_prefix_sum(prefix_sum, i, j-k+1, i, j+k)  # Сумма символов '#' в горизонтальной линии
        
        if vertical_sum == k*2+1 and horizontal_sum == k*2+1:
            max_possible_k = k
        else:
            break

    # Ограничиваем максимально возможный размер найденным максимальным значением
    if max_possible_k > current_largest_k:
        return max_possible_k
    else:
        return 0  # Если текущий максимальный размер больше, возвращаем 0 для оптимизации

def compute_prefix_sums_n(matrix):
    n, m = len(matrix), len(matrix[0])
    left = [[0] * m for _ in range(n)]
    #right = [[0] * m for _ in range(n)]
    up = [[0] * m for _ in range(n)]
    #down = [[0] * m for _ in range(n)]
    
    # Заполняем префиксные суммы для всех направлений
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == '#':
                left[i][j] = (left[i][j-1] if j > 0 else 0) + 1
                up[i][j] = (up[i-1][j] if i > 0 else 0) + 1
    #for i in range(n-1, -1, -1):
    #    for j in range(m-1, -1, -1):
    #        if matrix[i][j] == '#':
    #            right[i][j] = (right[i][j+1] if j < m-1 else 0) + 1
    #            down[i][j] = (down[i+1][j] if i < n-1 else 0) + 1

    return left, up

def check_center_element(matrix, i, j, k, prefix_sum_rectangle):
    if is_center_possible_with_prefix(matrix, i, j, k, prefix_sum_rectangle):
        return True
    return False

def is_within_grid(matrix, i, j, k):
    n, m = len(matrix), len(matrix[0])
    offset = k // 2
    top_left_i = i - offset
    top_left_j = j - offset
    bottom_right_i = i + offset
    bottom_right_j = j + offset

    if k % 2 == 0:
        bottom_right_i -= 1
        bottom_right_j -= 1

    return 0 <= top_left_i < n and 0 <= top_left_j < m and 0 <= bottom_right_i < n and 0 <= bottom_right_j < m

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
    total = prefix_sum[end_i + 1][end_j + 1] - prefix_sum[start_i][end_j + 1] - prefix_sum[end_i + 1][start_j] + prefix_sum[start_i][start_j]
    
    # Если общее количество '#' равно площади квадрата, то весь квадрат заполнен '#'
    return total == k * k


def is_center_possible(matrix, i, j, k):
    n, m = len(matrix), len(matrix[0])
    offset = 0 if k % 2 != 0 else 1

    start_i = i - k // 2 + offset
    end_i = i + k // 2
    start_j = j - k // 2 + offset
    end_j = j + k // 2
    
    # Проверяем наличие символа '#' в каждой клетке квадрата
    for dx in range(start_i, end_i + 1):
        for dy in range(start_j, end_j + 1):
            if dx < 0 or dx >= n or dy < 0 or dy >= m or matrix[dx][dy] != '#':
                return False
    return True

def check_all_arms(matrix, center_i, center_j, k, prefix_sum_rectangle):
    # Устанавливаем начальные точки для каждой "руки" на расстоянии k от центра
    starts = [
        (center_i - k, center_j),  # Вверх
        (center_i + k, center_j),  # Вниз
        (center_i, center_j - k),  # Влево
        (center_i, center_j + k)   # Вправо
    ]

    for start_i, start_j in starts:
        if not is_center_possible_with_prefix(matrix, start_i, start_j, k, prefix_sum_rectangle):
            return False
    return True


def find_max_plus_l(matrix, i, j, base_k, prefix_sum_rectangle):
    n, m = len(matrix), len(matrix[0])
    low, high = 0, base_k

    while low < high:
        mid = (low + high) // 2
        if is_within_grid(matrix, i, j, mid) and check_center_element(matrix, i, j, mid, prefix_sum_rectangle) and check_all_arms(matrix, i, j, mid, prefix_sum_rectangle):
            low = mid + 1
        else:
            high = mid
    
    return low - 1  # Возвращаем размер центрального элемента
    
def find_largest_expanded_plus(matrix, prefix_sum_rectangle):
    n, m = len(matrix), len(matrix[0])
    #left, right, up, down = compute_prefix_sums_n(matrix)
    largest_expanded_k = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != '#':
                continue
            #base_k = calculate_max_possible_plus_size(prefix_sum_rectangle, i, j, n, m, largest_expanded_k)
            #if base_k == 0:
            #    continue
            base_k = min(n, m)
            expanded_k = find_max_plus_l(matrix, i, j, base_k, prefix_sum_rectangle)
            largest_expanded_k = max(largest_expanded_k, expanded_k)
    
    return largest_expanded_k
print_grid(grid)
print("____________________")
prefix_sum_rectangle = build_prefix_sum_rectangle(grid)
print_grid(prefix_sum_rectangle)
ans = find_largest_expanded_plus(grid, prefix_sum_rectangle)

with open("output.txt", "w") as file:
    file.write(str(ans))