import heapq


with open("input.txt", "r") as reader:
    N, K = map(int, reader.readline().strip().split(" "))
    adj_list = {i: [] for i in range(1, N + 1)}
    for i in range(1, K + 1):
        A, B, L = map(int, reader.readline().strip().split(" "))
        adj_list[A].append((L, B))
        adj_list[B].append((L, A))

    S, F = map(int, reader.readline().strip().split(" "))


def dijkstra_algo(start, end, adj_list):
    seen_nodes = set()
    heap = []

    heapq.heappush(heap, (0, start))  # start from 0

    while heap:
        node_to_relax_score, node_to_relax_index = heapq.heappop(heap)

        if node_to_relax_index not in seen_nodes:
            seen_nodes.add(node_to_relax_index)

            if node_to_relax_index == end:
                return node_to_relax_score

            for score, index in adj_list[node_to_relax_index]:
                new_score = node_to_relax_score + score
                heapq.heappush(heap, (new_score, index))  # start from 0

    return -1


ans = dijkstra_algo(S, F, adj_list)


with open("output.txt", "w") as file:
    file.write(str(ans))
