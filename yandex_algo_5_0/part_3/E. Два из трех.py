with open("input.txt", "r") as reader:
    n = 3  # num of arrays
    lst_of_digits_sets = []
    for i in range(n):
        num_el = reader.readline().split()
        digit_lst = {int(num) for num in reader.readline().strip().split(" ")}
        lst_of_digits_sets.append(digit_lst)

first_union = lst_of_digits_sets[0] & lst_of_digits_sets[1]
second_union = lst_of_digits_sets[1] & lst_of_digits_sets[2]
third_union = lst_of_digits_sets[0] & lst_of_digits_sets[2]
combined_set = first_union | second_union | third_union

sorted_list = list(combined_set)
sorted_list.sort()

with open("output.txt", "w") as file:
    file.write(" ".join(str(num) for num in sorted_list))
