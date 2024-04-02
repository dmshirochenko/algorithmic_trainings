# Reading from the file
with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    graph_grid = []
    for i in range(n):
        vrtx_to_add = [int(i) for i in reader.readline().strip().split(" ")]
        graph_grid.append(vrtx_to_add)

# Function definitions from the provided code
def convert_to_adj_list(matrix):
    adj_list = {}
    for i, row in enumerate(matrix):
        connections = {j: weight for j, weight in enumerate(row) if weight != 0}
        if connections:
            adj_list[i] = connections
    return adj_list


def graph_calculate_cut_value_adj_list(adj_list, sets):
    cut_value = 0
    for vertex, edges in adj_list.items():
        for neighbor, weight in edges.items():
            if sets[vertex] != sets[neighbor]:
                cut_value += weight
    return cut_value // 2


def next_gray_code(current_gray_code):
    # Get the position of the rightmost set bit
    rightmost_set_bit = current_gray_code & -current_gray_code
    next_gray_code = current_gray_code ^ (rightmost_set_bit >> 1)
    return next_gray_code


def generate_gray_codes_iteratively(n):
    num_codes = 1 << n  # Total number of Gray codes for n bits
    return [i ^ (i >> 1) for i in range(num_codes)]


def update_cut_value_for_flip(adj_list, sets, vertex_to_flip, current_cut_value):
    # Calculate the change in cut value due to flipping a single vertex
    delta = 0
    for neighbor, weight in adj_list[vertex_to_flip].items():
        if sets[vertex_to_flip] == sets[neighbor]:  # Edge will be removed from cut
            delta -= weight
        else:  # Edge will be added to cut
            delta += weight
    return current_cut_value + delta


def find_max_cut_with_gray_codes(adj_list, n):
    max_cut_value = 0
    best_combination = [0] * n
    current_sets = [0] * n
    current_cut_value = 0
    previous_gray_code = 0

    for gray_code in generate_gray_codes_iteratively(n):
        changed_bit = gray_code ^ previous_gray_code
        if changed_bit != 0:
            vertex_to_flip = changed_bit.bit_length() - 1
            current_sets[vertex_to_flip] = 1 - current_sets[vertex_to_flip]
            current_cut_value = update_cut_value_for_flip(adj_list, current_sets, vertex_to_flip, current_cut_value)

            if current_cut_value > max_cut_value:
                max_cut_value = current_cut_value
                best_combination[:] = current_sets[:]

        previous_gray_code = gray_code

    return best_combination, max_cut_value


def main(n, graph_grid):
    adj_list = adj_list = convert_to_adj_list(graph_grid)
    best_sets, max_cut_value = find_max_cut_with_gray_codes(adj_list, n)
    partition_output = [1 + set_id for set_id in best_sets]

    return max_cut_value, partition_output


graph_max_cut_value, final_division = main(n, graph_grid)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(graph_max_cut_value) + "\n")
    file.write(" ".join(str(item) for item in final_division))
