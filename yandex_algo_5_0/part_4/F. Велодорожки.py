with open("input.txt", "r") as reader:
    cols, rows, num_of_broken_piles = map(int, reader.readline().strip().split(" "))
    broken_piles = {
        "rows": {},
        "cols": {}
    }
    for _ in range(num_of_broken_piles):
        x, y = map(int, reader.readline().strip().split(" "))
        x_to_add = x - 1
        y_to_add = y - 1
        if x_to_add not in broken_piles["rows"]:
            broken_piles["rows"][x_to_add] = set()
            broken_piles["rows"][x_to_add].add((x_to_add, y_to_add))
        else:
            broken_piles["rows"][x_to_add].add((x_to_add, y_to_add))
        
        if y_to_add not in broken_piles["cols"]:
            broken_piles["cols"][y_to_add] = set()
            broken_piles["cols"][y_to_add].add((x_to_add, y_to_add))
        else:
            broken_piles["cols"][y_to_add].add((x_to_add, y_to_add))

def print_matrix(matrix):
    for row in matrix:
        print(row)

def calculate_prefix_suffix_sums(broken_piles, n, m):
    prefix_sum_rows = [0] * n
    suffix_sum_rows = [0] * n
    prefix_sum_cols = [0] * m
    suffix_sum_cols = [0] * m

    for i in range(n):
        prefix_sum_rows[i] = prefix_sum_rows[i - 1] + (1 if i in broken_piles["rows"] else 0)
    for j in range(m):
        prefix_sum_cols[j] = prefix_sum_cols[j - 1] + (1 if j in broken_piles["cols"] else 0)

    for i in range(n - 2, -1, -1):
        suffix_sum_rows[i] = suffix_sum_rows[i + 1] + (1 if i in broken_piles["rows"] else 0)
    for j in range(m - 2, -1, -1):
        suffix_sum_cols[j] = suffix_sum_cols[j + 1] + (1 if j in broken_piles["cols"] else 0)

    return prefix_sum_rows, suffix_sum_rows, prefix_sum_cols, suffix_sum_cols

def check_width_possible(width, broken_piles, rows, cols):
    all_broken_tiles = set()

    for row_tiles in broken_piles['rows'].values():
        all_broken_tiles.update(row_tiles)
    
    for row_start in range(rows - width + 1):
        for col_start in range(cols - width + 1):
            covered_tiles = set()
            for r in range(row_start, row_start + width):
                covered_tiles.update(broken_piles['rows'].get(r, set()))
                
            for c in range(col_start, col_start + width):
                covered_tiles.update(broken_piles['cols'].get(c, set()))
            if all_broken_tiles.issubset(covered_tiles):
                return True

    return False


def binary_search_for_min_width(n, m, prefix_sum_rows, suffix_sum_rows, prefix_sum_cols, suffix_sum_cols):
    left, right = 1, max(n, m)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if check_width_possible(mid, broken_piles, n, m):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


# Пример использования
if __name__ == "__main__":
    #print(broken_piles)
    prefix_sum_rows, suffix_sum_rows, prefix_sum_cols, suffix_sum_cols = calculate_prefix_suffix_sums(broken_piles, rows, cols)
    binary_search_result = binary_search_for_min_width(rows, cols, prefix_sum_rows, suffix_sum_rows, prefix_sum_cols, suffix_sum_cols)
    #print('binary_search_result', binary_search_result)
    with open("output.txt", "w") as file:
        file.write(str(binary_search_result))
