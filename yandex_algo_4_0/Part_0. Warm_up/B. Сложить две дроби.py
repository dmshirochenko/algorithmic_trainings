# Reading from the file
with open("input.txt", "r") as reader:
    fraction_num_1, fraction_denom_1, fraction_num_2, fraction_denom_2 = map(int, reader.readline().split(" "))


def max_divider(a, b):
    if b % a == 0:
        return a

    for i in range(a, 1, -1):
        if b % i == 0 and a % i == 0:
            return i

    return False


sum_result_denom = fraction_denom_1 * fraction_denom_2

sum_result_num = (fraction_num_1 * (sum_result_denom // fraction_denom_1)) + (
    fraction_num_2 * (sum_result_denom // fraction_denom_2)
)


if sum_result_num > sum_result_denom:
    num_to_devide = max_divider(sum_result_denom, sum_result_num)
elif sum_result_num == sum_result_denom:
    num_to_devide = sum_result_num
else:
    num_to_devide = max_divider(sum_result_num, sum_result_denom)


if num_to_devide:
    sum_result_num = sum_result_num // num_to_devide
    sum_result_denom = sum_result_denom // num_to_devide

ans = sum_result_num, sum_result_denom

# Writing to the file
with open("output.txt", "w") as file:
    file.write(" ".join(str(item) for item in ans))
