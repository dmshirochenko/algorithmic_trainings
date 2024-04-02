import heapq

with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    S, F = map(int, reader.readline().strip().split(" "))
    R = int(reader.readline().strip())
    adj_list = {i: [] for i in range(1, N + 1)}
    for i in range(1, R + 1):
        FROM, WHEN_STARTS, TO, TIME_TO_ARRIVAL = map(int, reader.readline().strip().split(" "))
        adj_list[FROM].append((TIME_TO_ARRIVAL, TO, WHEN_STARTS))


def dijkstra_algo(start, end, adj_list):

    seen_nodes = set()
    heap = []
    heapq.heappush(heap, (0, 0, start))  # start from 0

    while heap:
        current_time, node_to_relax_score, node_to_relax_index = heapq.heappop(heap)
        # print("node_to_relax_score, node_to_relax_index, current_time", node_to_relax_score, node_to_relax_index, current_time)
        if node_to_relax_index not in seen_nodes:
            seen_nodes.add(node_to_relax_index)

            if node_to_relax_index == end:
                return current_time

            for time_to_spend, index, r_start_time in adj_list[node_to_relax_index]:
                # print("time_to_spend, index, r_start_time", time_to_spend, index, r_start_time)
                if r_start_time >= current_time:
                    new_time_to_spend = (time_to_spend - r_start_time) + (r_start_time - current_time)
                    new_current_time = current_time + new_time_to_spend
                    heapq.heappush(heap, (new_current_time, new_time_to_spend, index))  # start from 0

    return -1


ans = dijkstra_algo(S, F, adj_list)


with open("output.txt", "w") as file:
    file.write(str(ans))
