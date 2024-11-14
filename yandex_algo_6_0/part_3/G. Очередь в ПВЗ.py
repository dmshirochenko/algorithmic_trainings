from collections import deque

with open("input.txt", "r") as reader:
    time_close, serve_per_minute = map(int, reader.readline().split())
    num_clients = list(map(int, reader.readline().split()))

#print("time_close=", time_close, "serve_per_minute=", serve_per_minute, "num_clients=", num_clients)

def time_to_serve_all_clients(time_close, serve_per_minute, num_clients):
    curr_minute = 0
    curr_queue = 0
    time_spent = 0
    while True:
        if curr_minute == time_close:
            break
        #print(" begin curr_minute=", curr_minute, "curr_queue=", curr_queue, "time_spent=", time_spent)
        if len(num_clients) > curr_minute:
            curr_queue += num_clients[curr_minute]
        if curr_queue > 0:
            if curr_queue >= serve_per_minute:
                curr_queue -= serve_per_minute
                time_spent += serve_per_minute
            else:
                time_spent += curr_queue
                curr_queue = 0
            time_spent += curr_queue

        #print("curr_minute=", curr_minute, "curr_queue=", curr_queue, "time_spent=", time_spent)
        curr_minute += 1

    time_spent += curr_queue

    return time_spent

ans = time_to_serve_all_clients(time_close, serve_per_minute, num_clients)
#print("ans =", ans)
with open("output.txt", "w") as file:
    file.write(str(ans))