from collections import deque

with open("input.txt", "r") as reader:
    n, b = map(int, reader.readline().split())
    num_clients = list(map(int, reader.readline().split()))


def time_to_serve_all_clients(n, b, num_clients):
    queue = deque()
    time = 0

    for i in range(n):


ans = time_to_serve_all_clients(n, b, num_clients)
print("ans =", ans)
with open("output.txt", "w") as file:
    file.write(str(ans))