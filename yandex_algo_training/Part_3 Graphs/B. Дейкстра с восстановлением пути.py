import heapq


with open("input.txt", "r") as reader:
    N, S, F = map(int, reader.readline().strip().split(" "))
    adj_list = {i: [] for i in range(1, N + 1)}
    for i in range(1, N + 1):
        line_to_lst = [None] + [int(n) for n in reader.readline().strip().split(" ")]
        for j in range(1, len(line_to_lst)):
            if line_to_lst[j] != 0 and line_to_lst[j] != -1:
                adj_list[i].append((line_to_lst[j], j))


def dijkstra_algo(start, end, N, adj_list):
    path = [None] + [(float("inf"), None) for i in range(N)]
    seen_nodes = set()
    heap = []

    heapq.heappush(heap, (0, start))  # start from 0
    path[start] = (0, 0)

    while heap:
        node_to_relax_score, node_to_relax_index = heapq.heappop(heap)
        if node_to_relax_index == end:
            return path

        if node_to_relax_index not in seen_nodes:
            seen_nodes.add(node_to_relax_index)

            for score, index in adj_list[node_to_relax_index]:
                old_score, prev_index = path[index]
                new_score = node_to_relax_score + score
                if new_score < old_score:
                    path[index] = (new_score, node_to_relax_index)
                heapq.heappush(heap, (new_score, index))  # start from 0

    return -1


if S != F:
    path = dijkstra_algo(S, F, N, adj_list)
    if path == -1:
        ans = [path]
    else:
        ans = []
        index = F
        ans.append(index)
        while True:
            index = path[index][1]
            ans.append(index)
            if index == S:
                break

        ans.reverse()
else:
    ans = [S]


with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
