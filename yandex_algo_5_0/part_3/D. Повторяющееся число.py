import math

with open("input.txt", "r") as reader:
    n, k = map(int, reader.readline().strip().split(" "))
    digit_lst = [int(num) for num in reader.readline().strip().split(" ")]

hash_map_k = dict()
left = 0
ans = "NO"

for right in range(len(digit_lst)):
    # do logic here to add arr[right] to curr
    if digit_lst[right] not in hash_map_k:
        hash_map_k[digit_lst[right]] = 1
    else:
        hash_map_k[digit_lst[right]] += 1

    while len(hash_map_k) > k:
        # remove arr[left] from curr
        del hash_map_k[digit_lst[left]] 
        left += 1

    if hash_map_k[digit_lst[right]] > 1:
        ans = "YES"
        break
    
with open("output.txt", "w") as file:
    file.write(str(ans))