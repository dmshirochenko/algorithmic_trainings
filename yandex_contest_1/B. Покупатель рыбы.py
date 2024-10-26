# Reading from the file
with open("input.txt", "r") as reader:
    N, K = map(int, reader.readline().strip().split(" "))
    lst_of_fish_cost = list(map(int, reader.readline().strip().split(" ")))

index_days_covered = set()
count_of_fish_per_day = [0] * N
cost = 0

for i in range(N):
    current_day_fish_cost = lst_of_fish_cost[i]
    num_of_expensive_days = 0
    #print('current_day_fish_cost', current_day_fish_cost)
    for j in range(i, min(i + K, N)):
        #print('current day', current_day_fish_cost, 'fish_cost', lst_of_fish_cost[j])
        if current_day_fish_cost <= lst_of_fish_cost[j]:
            if j in index_days_covered:
                continue
            num_of_expensive_days += 1
            index_days_covered.add(j)
        else:
            break
    
    count_of_fish_per_day[i] = num_of_expensive_days
    cost += current_day_fish_cost * num_of_expensive_days

#print(cost)
#print(count_of_fish_per_day)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(cost))
    file.write('\n')
    file.write(" ".join(str(num) for num in count_of_fish_per_day))