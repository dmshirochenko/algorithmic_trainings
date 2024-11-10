with open("input.txt", "r") as reader:
    n = int(reader.readline())
    cities_cost_of_living_lst = list(map(int, reader.readline().split()))


def cities_to_move(cities_cost_of_living_lst):
    ans = [-1] * len(cities_cost_of_living_lst)
    stack = []

    stack.append((cities_cost_of_living_lst[0], 0))

    for i in range(1, len(cities_cost_of_living_lst)):
        if stack:
            while stack and stack[-1][0] > cities_cost_of_living_lst[i]:
                city_with_less_pricess = stack.pop()
                ans[city_with_less_pricess[1]] = i

            stack.append((cities_cost_of_living_lst[i], i))
        else:
            stack.append((cities_cost_of_living_lst[i], i))

    return ans


ans = cities_to_move(cities_cost_of_living_lst)

with open("output.txt", "w") as file:
    file.write(" ".join(map(str, ans)))
