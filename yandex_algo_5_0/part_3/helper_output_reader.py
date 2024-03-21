def read_lines(file_path):
    with open(file_path, "r") as reader:
        for line in reader:
            yield line.strip()

lst_my_output = []
lst_yandex_output = []
for line in read_lines("output.txt"):
    lst_my_output.append(line)

for line in read_lines("09 (3).a"):
    lst_yandex_output.append(line)


for i in range(len(lst_my_output)):
    if lst_my_output[i] != lst_yandex_output[i]:
        print(i + 1, 'lst_my_output', lst_my_output[i], 'lst_yandex_output', lst_yandex_output[i])
        