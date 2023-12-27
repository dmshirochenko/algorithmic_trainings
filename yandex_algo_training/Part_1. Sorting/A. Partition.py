with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    if N != 0:
        arr_1 = [int(n) for n in reader.readline().split(" ")]
    else:
        empty_line = reader.readline()
        arr_1 = []

    x = int(reader.readline())


def partition(predicate, arr_to_check, start=0, end=None):
    left = []
    equal = []
    right = []

    for item in arr_to_check:
        if item < predicate:
            left.append(item)
        elif item > predicate:
            right.append(item)
        elif item == predicate:
            equal.append(item)

    return len(left)


if N == 0:
    ans = [0, 0]
else:
    el_less_index = partition(x, arr_1)

    ans = [el_less_index, len(arr_1) - el_less_index]


with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
