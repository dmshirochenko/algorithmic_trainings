# Reading from the file
with open("input.txt", "r") as reader:
    P, V = map(int, reader.readline().split(" "))
    Q, M = map(int, reader.readline().split(" "))

#sort intervals
if (P - V) > (Q - M):
    first_interval = [Q - M, Q + M]
    second_interval = [P - V, P + V]
else:
    first_interval = [P - V, P + V]
    second_interval = [Q - M, Q + M]

merged_interval = []
#merging intervals
if first_interval[1] >= second_interval[0]:
    merged_interval = [first_interval[0], max(abs(first_interval[1]), abs(second_interval[1]))]

if merged_interval:
    ans = merged_interval[1] - merged_interval[0] + 1
else:
    ans = (first_interval[1] - first_interval[0] + 1) + (second_interval[1] - second_interval[0] + 1)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
