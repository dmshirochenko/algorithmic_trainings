with open("input.txt", "r") as reader:
    n = int(reader.readline())
    algo_interest_lst = list(map(int, reader.readline().split()))
    algo_helpfulness_lst = list(map(int, reader.readline().split()))
    mood_lst = list(map(int, reader.readline().split()))

"""
print('algo_interest_lst:', algo_interest_lst)
print('algo_helpfulness_lst:', algo_helpfulness_lst)
print('mood_lst:', mood_lst)
"""


def create_algo_lst(algo_interest_lst, algo_helpfulness_lst, mood_lst):
    algo_lst = []
    for i in range(n):
        algo_lst.append((i, algo_interest_lst[i], algo_helpfulness_lst[i], mood_lst[i]))
    return algo_lst


def sort_algo_lst(algo_lst, how_to_sort):
    if how_to_sort == "interest":
        return sorted(algo_lst, key=lambda x: (x[1], x[2], -x[0]))
    elif how_to_sort == "helpfulness":
        return sorted(algo_lst, key=lambda x: (x[2], x[1], -x[0]))


def combine_interest_helpfulness(n, algo_lst_1, algo_lst_2):
    new_lst = []
    for i in range(n):
        new_lst.append((i, algo_lst_1[i], algo_lst_2[i]))

    return new_lst


def choose_algo_to_study(algo_interest_lst, algo_helpfulness_lst, mood_lst):
    styded_algo = set()
    ans = []

    for mood in mood_lst:
        if mood == 0:
            while True:
                candidate = algo_interest_lst.pop()[0] + 1
                if candidate not in styded_algo:
                    styded_algo.add(candidate)
                    ans.append(candidate)
                    break
        else:
            while True:
                candidate = algo_helpfulness_lst.pop()[0] + 1
                if candidate not in styded_algo:
                    styded_algo.add(candidate)
                    ans.append(candidate)
                    break

    return ans


new_algo_sorted_by_interest = sort_algo_lst(
    create_algo_lst(algo_interest_lst, algo_helpfulness_lst, mood_lst), "interest"
)
new_algo_sorted_by_helpfulness = sort_algo_lst(
    create_algo_lst(algo_interest_lst, algo_helpfulness_lst, mood_lst), "helpfulness"
)
"""
print('new_algo_sorted_by_interest:', new_algo_sorted_by_interest)
print('new_algo_sorted_by_helpfulness:', new_algo_sorted_by_helpfulness)
"""
ans = choose_algo_to_study(new_algo_sorted_by_interest, new_algo_sorted_by_helpfulness, mood_lst)

with open("output.txt", "w") as file:
    # write as sting
    file.write(" ".join(map(str, ans)))
