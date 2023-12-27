with open("input.txt", "r") as reader:
    N = int(reader.readline())
    arr_to_sort = []
    for i in range(N):
        arr_to_sort.append(str(reader.readline().strip()))

file = open("output.txt", "w")
M = len(arr_to_sort[0])

initial_backet = {str(i): [] for i in range(10)}
all_baskets = []

for element in arr_to_sort:
    initial_backet[element[-1]].append(element)

all_baskets.append(initial_backet)

for i in range(M - 1):
    new_backet = {str(i): [] for i in range(10)}
    for index, item in all_baskets[i].items():
        for value in item:
            new_backet[value[-(i + 2)]].append(value)

    all_baskets.append(new_backet)


with open("output.txt", "w") as file:
    file.writelines("Initial array:\n")
    file.writelines(", ".join(str(item) for item in arr_to_sort))
    file.writelines("\n")
    phase_counter = 1
    for backet in all_baskets:
        file.writelines("**********\n")
        file.writelines(f"Phase {phase_counter}\n")
        for index, values in backet.items():
            if values:
                formatted_values = ", ".join(values)  # This turns the list into a string of comma-separated values.
                file.writelines(f"Bucket {index}: {formatted_values}\n")
            else:
                file.writelines(f"Bucket {index}: empty\n")

        phase_counter += 1

    file.writelines("**********\n")
    file.writelines("Sorted array:\n")
    flattened_values = [item for sublist in all_baskets[-1].values() for item in sublist]
    result = ", ".join(flattened_values)
    file.writelines(result)
