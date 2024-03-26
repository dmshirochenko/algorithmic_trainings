with open("input.txt", "r") as reader:
    n, m = map(int, reader.readline().strip().split(" "))
    orks_army = [int(num) for num in reader.readline().strip().split(" ")]
    requests_lst = []
    for i in range(m):
        n_colonels, sum_of_orks = map(int, reader.readline().strip().split(" "))
        requests_lst.append((n_colonels, sum_of_orks))

prefix_sum = [0]
for i in range(len(orks_army)):
    prefix_sum.append(prefix_sum[-1] + orks_army[i])

def binary_search(left, right, prefix_sum, interval, sum_of_orks):
    index = -1

    while left < right:
        mid_index = (left + right) // 2
        if (prefix_sum[mid_index] - prefix_sum[mid_index - interval]) > sum_of_orks:
            right = mid_index
        elif (prefix_sum[mid_index] - prefix_sum[mid_index - interval]) < sum_of_orks:
            left = mid_index + 1
        else:
            index = mid_index
            break
   
    return index

#binary search
ans_lst_binary = []
for request in requests_lst:
    interval, sum_of_orks = request
    ans = binary_search(interval, len(prefix_sum), prefix_sum, interval, sum_of_orks)
    if ans != -1:
        ans_lst_binary.append((ans - interval) + 1)
    else:
        ans_lst_binary.append(-1)

#linear search
ans_lst = []
for request in requests_lst:
    interval, sum_of_orks = request
    ans = -1
    for i in range(interval, len(prefix_sum)):
        if (prefix_sum[i] - prefix_sum[i - interval]) == sum_of_orks:
            ans = i - interval
            break
        elif (prefix_sum[i] - prefix_sum[i - interval]) > sum_of_orks:
            break
    
    if ans != -1:
        ans_lst.append(ans + 1)
    else:
        ans_lst.append(-1)

with open("output.txt", "w") as file:
    file.write(" ".join(str(num) for num in ans_lst_binary))