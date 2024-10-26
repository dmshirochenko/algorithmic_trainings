from collections import deque

# Reading from the file
with open("input.txt", "r") as reader:
    number_of_moves = int(reader.readline().strip())
    moves = []
    for _ in range(number_of_moves):
        x, y = map(int, reader.readline().strip().split(" "))
        moves.append((int(x), int(y)))

LINE_LEN_TO_WIN = 5
POSSIBLE_MOVES = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

def get_graph(moves):
    graph = {}
    moves = set(moves)
    
    for move in moves:
        x, y = move
        graph[(x, y)] = []
        for dx, dy in POSSIBLE_MOVES:
            new_x, new_y = x + dx, y + dy
            if (new_x, new_y) in moves:
                graph[(x, y)].append((new_x, new_y))
    return graph

def bfs(node_to_check, graph):
    queue = deque([node_to_check])
    seen = {node_to_check}
    max_level = 0

    while queue:
        current_length = len(queue)
        max_level += 1
        for _ in range(current_length):
            node = queue.popleft()
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

    return max_level


if __name__ == "__main__":
    moves_player_one = []
    moves_player_two = []

    for index in range(len(moves)):
        if index % 2 == 0:
            moves_player_one.append(moves[index])
        else:
            moves_player_two.append(moves[index])

max_level_player_one = 0
max_level_player_two = 0

is_player_one_wins = False
is_player_two_wins = False
is_inattention = False
last_check_index_player_one = 0
last_check_index_player_two = 0

for i in range(max(len(moves_player_one), len(moves_player_two))):
    if i < len(moves_player_one):
        print('moves_player_one[:i]', moves_player_one[:i + 1])
        graph_player_one = get_graph(moves_player_one[:i + 1])
        for node in graph_player_one:
            max_level_player_one = max(max_level_player_one, bfs(node, graph_player_one))
    
    if max_level_player_one >= LINE_LEN_TO_WIN:
        is_player_one_wins = True
        last_check_index_player_one = i
        last_check_index_player_two = i - 1
        break
        

    if i < len(moves_player_two):
        print('moves_player_two[:i]', moves_player_two[:i + 1])
        graph_player_two = get_graph(moves_player_two[:i + 1])
        for node in graph_player_one:
            max_level_player_two = max(max_level_player_two, bfs(node, graph_player_one))

    if max_level_player_two >= LINE_LEN_TO_WIN:
        is_player_two_wins = True
        last_check_index_player_one = i
        last_check_index_player_two = i
        break
        


if last_check_index_player_one < len(moves_player_one) - 1 or last_check_index_player_two < len(moves_player_two) - 1:
    is_inattention = True

if is_inattention:
    ans = "Inattention"
elif is_player_one_wins:
    ans = "First"
elif is_player_two_wins:
    ans = "Second"
else:
    ans = "Draw"

# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)