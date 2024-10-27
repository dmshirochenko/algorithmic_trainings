# Reading from the file
with open("input.txt", "r") as reader:
    N = int(reader.readline())
    air_conditioners_tests = []
    for i in range(N):
        air_conditioners_tests.append(list(reader.readline().split()))


def heat(t_room, t_cond):
    if t_room >= t_cond:
        return t_room
    else:
        return t_cond

def freeze(t_room, t_cond):
    if t_room <= t_cond:
        return t_room
    else:
        return t_cond

def auto(t_room, t_cond):
    return t_cond

def fan(t_room, t_cond):
    return t_room

air_conditioners_modes = {
    "heat": heat,
    "freeze": freeze,
    "auto": auto,
    "fan": fan
}


def air_conditioners(air_conditioners_tests):
    ans = []
    for test in air_conditioners_tests:
        t_room = int(test[0])
        mode = test[2]
        t_cond = int(test[1])
        ans.append(air_conditioners_modes[mode](t_room, t_cond))
    return ans

ans = air_conditioners(air_conditioners_tests)
print(ans)  
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))

#generate test cases for the solution as a list of tuples N = 20 
# it could ne -50 <= t_room, t_cond <= 50
# it could be one of the modes: heat, freeze, auto, fan
#generate all possible test cases as text file
#run the solution on each test case
"""
1. heat
2. freeze
3. auto
4. fan
20
-50 50 heat
50 -50 freeze
50 50 auto
50 50 fan
-50 -50 heat
-50 -50 freeze
-50 -50 auto
-50 -50 fan
-50 50 heat
-50 50 freeze
-50 50 auto
-50 50 fan
50 -50 heat
50 -50 freeze
50 -50 auto
50 -50 fan
50 50 heat
50 50 freeze
50 50 auto
50 50 fan
"""
