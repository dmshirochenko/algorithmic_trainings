# Reading from the file
with open("input.txt", "r") as reader:
    N, M = reader.readline().split(" ")
    sequence = [int(n) for n in reader.readline().split(" ")]
    request_list = []
    for i in range(int(M)):
        l, r = reader.readline().split(" ")
        request_list.append([int(l), int(r)])

ans = []

for l, r in request_list:
    seq_to_check = sequence[l : r + 1]
    if len(seq_to_check) == 1:
        ans.append("NOT FOUND")
        continue

    min_element = seq_to_check[0]
    other_element = -1

    for i in range(1, len(seq_to_check)):
        if min_element > seq_to_check[i]:
            other_element = min_element
            min_element = seq_to_check[i]
        elif min_element != seq_to_check[i]:
            other_element = seq_to_check[i]

    if other_element != -1:
        ans.append(other_element)
    else:
        ans.append("NOT FOUND")

# Writing to the file
with open("output.txt", "w") as file:
    for item in ans:
        file.write("%s\n" % item)
