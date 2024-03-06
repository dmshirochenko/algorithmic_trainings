import math

with open("input.txt", "r") as reader:
    N, K = map(int, reader.readline().strip().split(" "))
    fish_price_lst = [int(price) for price in reader.readline().strip().split(" ")]


def max_prof_finder(input_lst, K):
    max_profit = 0

    if len(input_lst) == 1:
        return max_profit
    
    K = min(K + 1, len(input_lst))

    for min_element_index in range(len(input_lst)):
        end_index = min(len(input_lst), min_element_index + K)
        for max_element_index in range(min_element_index + 1, end_index):
            curr_profit = input_lst[max_element_index] - input_lst[min_element_index]
            max_profit = max(max_profit, curr_profit)
            
    return max_profit

ans = max_prof_finder(fish_price_lst, K)

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))