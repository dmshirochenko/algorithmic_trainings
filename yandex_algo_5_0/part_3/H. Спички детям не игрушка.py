import math
from math import sqrt

import matplotlib.pyplot as plt

with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    dots_coord_before = []
    dots_coord_after = []
    
    #dots_coord_before
    for i in range(N):
        x_1, y_1, x_2, y_2 = map(int, reader.readline().strip().split(" "))
        dots_coord_before.append((x_1, y_1, x_2, y_2 ))

    #dots_coord_after
    for i in range(N):
        x_1, y_1, x_2, y_2 = map(int, reader.readline().strip().split(" "))
        dots_coord_after.append((x_1, y_1, x_2, y_2 ))

def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return float('inf')
    return (y2 - y1) / (x2 - x1)

def calculate_length(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def compare_lines(p1, p2, p3, p4):
    slope1 = calculate_slope(*p1, *p2)
    slope2 = calculate_slope(*p3, *p4)
    length1 = calculate_length(*p1, *p2)
    length2 = calculate_length(*p3, *p4)
    
    return slope1 == slope2 and length1 == length2

def calculate_midpoint(x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def calculate_dx_dy(x1, y1, x2, y2, x3, y3, x4, y4):
    xm1, ym1 = calculate_midpoint(x1, y1, x2, y2)
    xm2, ym2 = calculate_midpoint(x3, y3, x4, y4)

    dx = xm2 - xm1
    dy = ym2 - ym1
    
    return dx, dy

def draw_plot(lines, name):
    plt.figure(figsize=(8, 6))

    for line in lines:
        x_values = [line[0], line[2]]
        y_values = [line[1], line[3]]
        plt.plot(x_values, y_values, marker='o')

    # labels
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plot_name = 'Lines ' + name
    plt.title(plot_name)
    plt.grid(True)
    

possible_dx_dy = dict()

for line_before in dots_coord_before:
    x1, y1 , x2, y2 = line_before
    p1 = (x1, y1)
    p2 = (x2, y2)
    for line_after in dots_coord_after:
        x3, y3, x4, y4 = line_after
        p3 = (x3, y3)
        p4 = (x4, y4)
        if compare_lines(p1, p2, p3, p4):
            dx, dy = calculate_dx_dy(x1, y1, x2, y2, x3, y3, x4, y4)
            if (dx, dy) not in possible_dx_dy:
                possible_dx_dy[(dx, dy)] = [(line_before, line_after)]
            else:
                possible_dx_dy[(dx, dy)].append((line_before, line_after))

max_num_of_lines = -math.inf


for line_sets in possible_dx_dy.values():
    max_num_of_lines = max(max_num_of_lines, len(line_sets))

draw_plot(dots_coord_before, "before")
draw_plot(dots_coord_after, "after")
plt.show()

if max_num_of_lines != -math.inf:
    ans = N - max_num_of_lines
else:
    ans = N

with open("output.txt", "w") as file:
    file.write(str(ans))