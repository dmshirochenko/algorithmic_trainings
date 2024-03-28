with open("input.txt", "r") as reader:
    m, n, num_of_broken_piles = map(int, reader.readline().strip().split(" "))
    broken_piles = {tuple(map(int, reader.readline().strip().split(" "))) for _ in range(num_of_broken_piles)}


def print_matrix(matrix):
    for row in matrix:
        print(row)

def add_broken_piles_to_matrix(matrix, broken_piles):
    for pile in broken_piles:
        matrix[pile[1] - 1][pile[0] - 1] = 1

def max_min_broken_pile_cols(broken_piles):
    max_pile = None
    min_pile = None
    for pile in broken_piles:
        if max_pile is None or pile[0] > max_pile[0]:
            max_pile = pile
        if min_pile is None or pile[0] < min_pile[0]:
            min_pile = pile
    
    max_pile_zero_index = (max_pile[0] - 1, max_pile[1] - 1)
    min_pile_zero_index = (min_pile[0] - 1, min_pile[1] - 1)
    return max_pile_zero_index, min_pile_zero_index

def max_min_broken_pile_rows(broken_piles):
    max_pile = None
    min_pile = None
    for pile in broken_piles:
        if max_pile is None or pile[1] > max_pile[1]:
            max_pile = pile
        if min_pile is None or pile[1] < min_pile[1]:
            min_pile = pile

    max_pile_zero_index = (max_pile[0] - 1, max_pile[1] - 1)
    min_pile_zero_index = (min_pile[0] - 1, min_pile[1] - 1)
    return min_pile_zero_index, min_pile

def are_all_coords_covered(coords, w, n, m):
    #print('num of rows', n, 'num of cols', m)
    #print('coords', coords)
    for horizontal_start_row in range(n - w + 1):
        horizontal_end_row = horizontal_start_row + w
        for vertical_start_col in range(m - w + 1):
            vertical_end_col = vertical_start_col + w

            if all(
                (horizontal_start_row <= (row - 1) < horizontal_end_row) or
                (vertical_start_col <= (col - 1) < vertical_end_col)
                for col, row in coords
            ):
                return True
    return False

def binary_search(left, right, broken_piles, n, m):
    while left < right:
        mid = (left + right) // 2
        all_covered = are_all_coords_covered(broken_piles, mid, n, m)
        if all_covered:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    max_pile_cols, min_pile_cols = max_min_broken_pile_cols(broken_piles)
    max_pile_rows, min_pile_rows = max_min_broken_pile_rows(broken_piles)

    #add to set coords to look for
    coord_set = set()
    coord_set.add(max_pile_cols)
    coord_set.add(min_pile_cols)
    coord_set.add(max_pile_rows)
    coord_set.add(min_pile_rows)

    """
    for i in range(min(n, m) + 1):
        all_covered = are_all_coords_covered(broken_piles, i, n, m)
        if all_covered:
            break
    print(f"All coordinates covered by lines of width {i}: {all_covered}")
    """

    binary_search_result = binary_search(1, min(n, m), broken_piles, n, m)

    #print(f"Binary search result: {binary_search_result}")

    with open("output.txt", "w") as file:
        file.write(str(binary_search_result))