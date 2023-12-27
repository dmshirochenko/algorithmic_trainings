# Reading from the file
with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())

combinations = []


def all_combination(numbers, start=0):
    if start == len(numbers) - 1:
        string_to_add = "".join(str(i) for i in numbers)
        combinations.append(string_to_add)

    for i in range(start, len(numbers)):
        numbers[start], numbers[i] = numbers[i], numbers[start]
        all_combination(numbers, start + 1)
        numbers[start], numbers[i] = numbers[i], numbers[start]


n_num = [i for i in range(1, n + 1)]
all_combination(n_num)
combinations.sort()


# Reading from the file
with open("output.txt", "w") as file:
    file.write("\n".join(str(item) for item in combinations))
