import math

with open("input.txt", "r") as reader:
    n = int(reader.readline().strip())
    test_cases = []
    for i in range(n):
        num_elements = int(reader.readline().strip())
        elements = [int(num) for num in reader.readline().strip().split(" ")]
        test_cases.append(elements)
        elements = []

ans = []

for el in test_cases:
    curr_len = 0
    sub_lst = []
    curr_min_element = math.inf
    for right in range(len(el)):
        curr_min_element = min(curr_min_element, el[right])
        curr_len += 1
        if curr_min_element <= curr_len:
            if el[right] == 1:
                if curr_len > 1:
                    sub_lst.append(curr_len - 1)
                sub_lst.append(1)
                curr_len = 0
                curr_min_element = math.inf
            elif curr_min_element == el[right]:
                if el[right] == curr_len:
                    sub_lst.append(curr_len)
                    curr_len = 0
                    curr_min_element = math.inf
                else:
                    sub_lst.append(curr_len - 1)
                    curr_len = 1
                    curr_min_element = el[right]
            else:
                sub_lst.append(curr_len)
                curr_len = 0
                curr_min_element = math.inf
    else:
        if curr_len > 0:
            sub_lst.append(curr_len)

    ans.append(sub_lst)

# Writing to the file
with open("output.txt", "w") as file:
    for k in ans:
        file.write(str(len(k)))
        file.write("\n")
        line_to_add = " ".join(str(curr_len) for curr_len in k) + "\n"
        file.write(line_to_add)
