with open("input.txt", "r") as reader:
    N = int(reader.readline())
    test_cases = []
    for i in range(N):
        test_cases.append([int(n) for n in reader.readline().split(" ")])

"""
def group_split(students_per_group, students):
    dp = [0] + [students + 1] * students


    for i in range(1, students + 1):
        for student in students_per_group:
            if i >= student:
                dp[i] = min(dp[i], dp[i - student] + 1)

    return "YES" if dp[students] <= students else "NO"

"""


def can_divide_students(n, a, b):
    if a > n:
        return "NO"

    k_min = n // b
    k_max = n // a

    for k in range(k_min, k_max + 1):
        if a * k <= n <= b * k:
            return "YES"

    return "NO"


for test in test_cases:
    students, a, b = test
    print(can_divide_students(students, a, b))
