# Reading from the file
with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())


def is_safe(row, col, banned_cols, banned_diagonals_positive, banned_diagonals_negative):
    return (
        col not in banned_cols
        and (row + col) not in banned_diagonals_positive
        and (row - col) not in banned_diagonals_negative
    )


def count_ways_to_place_dinos(n, row, banned_cols, banned_diagonals_positive, banned_diagonals_negative):
    if row == n:
        return 1

    num_ways = 0
    for col in range(n):
        if is_safe(row, col, banned_cols, banned_diagonals_positive, banned_diagonals_negative):
            banned_cols.add(col)
            banned_diagonals_positive.add(row + col)
            banned_diagonals_negative.add(row - col)

            num_ways += count_ways_to_place_dinos(
                n, row + 1, banned_cols, banned_diagonals_positive, banned_diagonals_negative
            )

            banned_cols.remove(col)
            banned_diagonals_positive.remove(row + col)
            banned_diagonals_negative.remove(row - col)

    return num_ways


def main(n):
    return count_ways_to_place_dinos(n, 0, set(), set(), set())


ans = main(n)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
