import math
import itertools

with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    points_lst = list()

    for i in range(N):
        x, y = map(int, reader.readline().strip().split(" "))
        points_lst.append((x, y))


def find_square_vertices(diagonal_point1, diagonal_point2):
    x1, y1 = diagonal_point1
    x3, y3 = diagonal_point2

    center_x = (x1 + x3) / 2
    center_y = (y1 + y3) / 2

    half_delta_x = (x3 - x1) / 2
    half_delta_y = (y3 - y1) / 2

    vertex_B_x = center_x - half_delta_y
    vertex_B_y = center_y + half_delta_x

    vertex_D_x = center_x + half_delta_y
    vertex_D_y = center_y - half_delta_x

    return [(vertex_B_x, vertex_B_y), (vertex_D_x, vertex_D_y)]


def has_no_decimal_part(point):
    x, y = point
    return x % 1 == 0 and y % 1 == 0


points_set = set(points_lst)
min_points_to_add = math.inf
possible_points = []

unique_pairs = list(itertools.combinations(points_lst, 2))

for point_A, point_C in unique_pairs:
    is_points_decimal = False
    candidate_points = find_square_vertices(point_A, point_C)
    curr_points_to_add = 0
    curr_poinst_lst = []
    for point in candidate_points:
        if has_no_decimal_part(point):
            if point not in points_set:
                curr_points_to_add += 1
                curr_poinst_lst.append(point)
        else:
            is_points_decimal = True
            break
    if not is_points_decimal and curr_points_to_add < min_points_to_add:
        min_points_to_add = curr_points_to_add
        possible_points = curr_poinst_lst[:]

with open("output.txt", "w") as file:
    file.write(str(min_points_to_add))
    file.write("\n")
    for point in possible_points:
        file.write(" ".join(str(int(coor)) for coor in point))
        file.write("\n")
