# Reading from the file
with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    matrix = []
    for i in range(N):
        lst_to_add = [int(i) for i in reader.readline().strip().split(" ")]
        matrix.append(lst_to_add)


def shortest_cycle(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    current_path = [0]

    def backtrack():
        if len(current_path) == num_vertices:
            if graph[current_path[-1]][current_path[0]] > 0:
                return (
                    sum(graph[current_path[i]][current_path[i + 1]] for i in range(num_vertices - 1))
                    + graph[current_path[-1]][current_path[0]]
                )
            else:
                return float("inf")

        min_cycle_cost = float("inf")
        for next_vertex in range(1, num_vertices):
            if not visited[next_vertex] and graph[current_path[-1]][next_vertex] > 0:
                current_path.append(next_vertex)
                visited[next_vertex] = True
                cost = backtrack()
                min_cycle_cost = min(min_cycle_cost, cost)
                current_path.pop()
                visited[next_vertex] = False

        return min_cycle_cost

    visited[0] = True
    shortest_hamiltonian_cycle = backtrack()
    return shortest_hamiltonian_cycle if shortest_hamiltonian_cycle != float("inf") else -1


def main(n, graph):
    if n == 1:
        return 0
    return shortest_cycle(graph)


ans = main(N, matrix)

with open("output.txt", "w") as writer:
    writer.write(str(ans))
