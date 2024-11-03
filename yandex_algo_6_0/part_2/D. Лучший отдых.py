with open('input.txt', 'r') as reader:
    n, k = map(int, reader.readline().split())
    tasks = list(map(int, reader.readline().split()))

# sort tasks
tasks.sort()
#print("n=", n, "k=", k)
#print("tasks=", tasks)
left = 0
right = 1
num_of_days_to_complete = 0

while left < n:
    if right < n and tasks[right] - tasks[left] <= k:
        #print("not possible to add tasks[right]=", tasks[right], right, "tasks[left]=", tasks[left], left)
        right += 1
    else:
        #print( "tasks[left]=", tasks[left])
        num_of_days_to_complete = max(num_of_days_to_complete, right - left)
        left += 1

    
if n == 1:
    ans = 1
else:
    ans = num_of_days_to_complete
#print("ans=", ans)
with open("output.txt", "w") as file:
    file.write(str(ans))