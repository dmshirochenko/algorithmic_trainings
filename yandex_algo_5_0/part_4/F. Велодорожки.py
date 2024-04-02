import math

with open("input.txt", "r") as reader:
    w, h, num_of_broken_piles = map(int, reader.readline().strip().split(" "))
    broken_piles = []
    for i in range(num_of_broken_piles):
        x, y = map(int, reader.readline().strip().split(" "))
        broken_piles.append((x, y))


def print_matrix(matrix):
    for row in matrix:
        print(row)


def check_if_lines_are_covered(broken_piles, m, n, prefmin, prefmax, sufmin, sufmax):
    r = 0
    pmx = -(10**9)
    pmn = 10**9
    for i in range(n):
        while r < n and broken_piles[r][0] < broken_piles[i][0] + m:
            r += 1
        mx = pmx
        mn = pmn
        if r != n:
            mx = max(mx, sufmax[r])
            mn = min(mn, sufmin[r])
        if mx - mn < m:
            return True
        pmx = prefmax[i]
        pmn = prefmin[i]

    return False


def pref_sufix_preparation(broken_piles, n):
    prefmin = [broken_piles[0][1]] * n
    prefmax = [broken_piles[0][1]] * n
    sufmin = [broken_piles[-1][1]] * n
    sufmax = [broken_piles[-1][1]] * n

    for i in range(1, n):
        prefmin[i] = min(prefmin[i - 1], broken_piles[i][1])
        prefmax[i] = max(prefmax[i - 1], broken_piles[i][1])

    for i in range(n - 2, -1, -1):
        sufmin[i] = min(sufmin[i + 1], broken_piles[i][1])
        sufmax[i] = max(sufmax[i + 1], broken_piles[i][1])

    return prefmin, prefmax, sufmin, sufmax


def binary_search(broken_piles, w, h, num_of_broken_piles, prefmin, prefmax, sufmin, sufmax):
    left = 0
    right = min(w, h)
    while left < right:
        mid = (left + right) // 2
        all_covered = check_if_lines_are_covered(
            broken_piles, mid, num_of_broken_piles, prefmin, prefmax, sufmin, sufmax
        )
        if all_covered:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == "__main__":
    broken_piles.sort()
    prefmin, prefmax, sufmin, sufmax = pref_sufix_preparation(broken_piles, num_of_broken_piles)
    ans = binary_search(broken_piles, w, h, num_of_broken_piles, prefmin, prefmax, sufmin, sufmax)
    with open("output.txt", "w") as file:
        file.write(str(ans))
