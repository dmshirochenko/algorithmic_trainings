def max_mult(n, a):
    a.sort()
    if a[0] >= 0:
        return a[-1] * a[-2]
    if a[-1] <= 0:
        return a[-1] * a[-2]
    return max(a[0] * a[1], a[-1] * a[-2])

"""
#generate a test cases for the solution as a list of tuples N = 20
#Number of test cases = 20
#Possible number of digits 2 < K < 10
#POssible digits range -100 < ai < 100

20
2 -15 1
2 15 25
2 100 -100
2 0 7
2 7 -9
3 -1 0 1
3 -10 -10 0
3 0 10 10
3 0 0 0
3 15 -25 1
3 15 -25 5
3 15 25 -25
3 15 25 2
4 16 17 13 12
4 -3 3 0 -4
4 12 -13 11 -11
4 100 100 100 100
5 -1 2 6 -8 -11
6 14 15 -2 11 13 -17
10 1 2 3 4 5 6 7 8 9 10
"""







