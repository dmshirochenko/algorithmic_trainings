with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    rope_len_lst = [int(price) for price in reader.readline().strip().split(" ")]

ans = 0

total_len_on_table = 0
max_rope_on_table = 0
totat_len_without_max = 0

for rope in rope_len_lst:
    max_rope_on_table = max(max_rope_on_table, rope)
    total_len_on_table += rope

totat_len_without_max = total_len_on_table - max_rope_on_table

if max_rope_on_table > totat_len_without_max:
    ans = max_rope_on_table - totat_len_without_max
else:
    ans = total_len_on_table

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))