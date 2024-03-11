import math

with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    berries_lst_possitive_diff = []
    berries_lst_negative_diff = []
    max_drop_berry_between_postive = -math.inf
    last_drop_berry_positive = None
    max_increase_between_negative = -math.inf
    first_drop_berry_negative = None
    for i in range(N):
        up, down = map(int, reader.readline().strip().split(" "))
        if (up - down) >= 0:
            berries_lst_possitive_diff.append(((up - down), up, down, i + 1))
            if down > max_drop_berry_between_postive:
                max_drop_berry_between_postive = down
                last_drop_berry_positive = ((up - down), up, down, i + 1)
        else:
            berries_lst_negative_diff.append(((up - down), up, down, i + 1))
            if up > max_increase_between_negative:
                max_increase_between_negative = up
                first_drop_berry_negative = ((up - down), up, down, i + 1)

sum = 0
index_order = []

if first_drop_berry_negative is None:
    max_drop_berry = last_drop_berry_positive
elif last_drop_berry_positive is None:
    max_drop_berry = first_drop_berry_negative
elif first_drop_berry_negative[1] > last_drop_berry_positive[2]:
    max_drop_berry = first_drop_berry_negative
else:
    max_drop_berry = last_drop_berry_positive

for berry in berries_lst_possitive_diff:
    if berry == max_drop_berry:
        continue
    diff, up, down, index = berry
    sum += up
    sum -= down
    index_order.append(str(index))

# add max drop
sum += max_drop_berry[1]
index_order.append(str(max_drop_berry[3]))

# add negative berries
for berry in berries_lst_negative_diff:
    if berry == max_drop_berry:
        continue
    diff, up, down, index = berry
    index_order.append(str(index))

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(sum))
    file.write("\n")
    file.write(str(" ".join(index_order)))
