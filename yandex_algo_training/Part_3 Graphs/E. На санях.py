import heapq


def read_input():
    n = int(input().strip())
    transfer = [0] * n
    velocity = [0] * n
    for i in range(n):
        transfer[i], velocity[i] = map(int, input().strip().split())

    distances = [input().strip() for _ in range(n - 1)]
    return n, transfer, velocity, distances


def create_graphs(n, distances, transfer, velocity):
    time_matrix = [[float("inf") if i != j else 0 for j in range(n)] for i in range(n)]
    dist_graph = {i: [] for i in range(n)}

    for dist in distances:
        city_from, city_to, distance = map(int, dist.split())
        time_matrix[city_from - 1][city_to - 1] = distance / velocity[city_from - 1] + transfer[city_from - 1]
        time_matrix[city_to - 1][city_from - 1] = distance / velocity[city_to - 1] + transfer[city_to - 1]
        dist_graph[city_from - 1].append((city_to - 1, distance))
        dist_graph[city_to - 1].append((city_from - 1, distance))

    return time_matrix, dist_graph


def bfs(graph, node_from, node_to):
    if node_from == node_to:
        return 0
    queue = [(node_from, 0)]
    visited = [False] * len(graph)
    visited[node_from] = True

    while queue:
        curr_node, curr_dist = queue.pop(0)
        for new_node, new_dist in graph[curr_node]:
            if new_node == node_to:
                return curr_dist + new_dist
            if not visited[new_node]:
                queue.append((new_node, curr_dist + new_dist))
                visited[new_node] = True


def update_time_matrix(time_matrix, dist_graph, velocity, transfer):
    n = len(time_matrix)
    for i in range(n):
        for j in range(i, n):
            if time_matrix[i][j] == float("inf"):
                new_dist = bfs(dist_graph, i, j)
                time_matrix[i][j] = new_dist / velocity[i] + transfer[i]
                time_matrix[j][i] = new_dist / velocity[j] + transfer[j]


def dijkstra(time_matrix):
    n = len(time_matrix)
    dist = [float("inf")] * n
    dist[0] = 0
    min_values = []
    heapq.heapify(min_values)
    heapq.heappush(min_values, (0, 0, None))  # distance, vertex, prev_vertex
    visited = [False] * n
    prev = [None] * n

    while min_values:
        curr_dist, curr, prev_c = heapq.heappop(min_values)
        if visited[curr]:
            continue
        visited[curr] = True
        dist[curr] = curr_dist
        prev[curr] = prev_c
        for j in range(n):
            if j != curr:
                heapq.heappush(min_values, (time_matrix[j][curr] + curr_dist, j, curr))

    return dist, prev


def find_longest_path(dist, prev):
    max_dist = max(dist)
    way = [dist.index(max_dist)]
    while prev[way[-1]] is not None:
        way.append(prev[way[-1]])
    return max_dist, way


def main():
    n, transfer, velocity, distances = read_input()
    time_matrix, dist_graph = create_graphs(n, distances, transfer, velocity)
    update_time_matrix(time_matrix, dist_graph, velocity, transfer)
    dist, prev = dijkstra(time_matrix)
    max_dist, way = find_longest_path(dist, prev)
    print(f"{max_dist:.10f}")
    print(" ".join(map(str, [i + 1 for i in reversed(way)])))


if __name__ == "__main__":
    main()
