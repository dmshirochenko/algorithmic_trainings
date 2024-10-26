import math

# Reading from the file
with open("input.txt", "r") as reader:
    num_blue_tshirts = int(reader.readline())
    num_red_tshirts = int(reader.readline())
    num_blue_socks = int(reader.readline())
    num_red_socks = int(reader.readline())

def check_min_amount_of_clotches(num_blue_tshirts, num_red_tshirts, num_blue_socks, num_red_socks):
    tries_to_picks = {"blue_tshirt_first": None, "red_tshirt_first": None, "blue_socks_first": None, "red_socks_first": None}

    #try to pick blue tshirt first
    if num_blue_tshirts != 0:
        ans_blue_tshirt_first = {"min_tshirts": 0, "min_socks": 0, "sum": 0}
        if num_blue_tshirts <= num_red_tshirts:
            ans_blue_tshirt_first["min_tshirts"] = num_red_tshirts + 1
            ans_blue_tshirt_first["min_socks"] = 1
        elif num_red_tshirts == 0:
            ans_blue_tshirt_first["min_tshirts"] = 1
            ans_blue_tshirt_first["min_socks"] = num_red_socks + 1
        elif num_red_socks == 0:
            ans_blue_tshirt_first["min_tshirts"] = num_red_tshirts + 1
            ans_blue_tshirt_first["min_socks"] = 1
        elif num_blue_socks == 0:
            pass
        else:    
            ans_blue_tshirt_first["min_tshirts"] = num_red_tshirts + 1
            ans_blue_tshirt_first["min_socks"] = num_red_socks + 1

        tries_to_picks["blue_tshirt_first"] = ans_blue_tshirt_first
        tries_to_picks["blue_tshirt_first"]["sum"] = ans_blue_tshirt_first["min_tshirts"] + ans_blue_tshirt_first["min_socks"]

    #try to pick red tshirt first
    if num_red_tshirts != 0:
        ans_red_tshirt_first = {"min_tshirts": 0, "min_socks": 0, "sum": 0}
        if num_red_tshirts <= num_blue_tshirts:
            ans_red_tshirt_first["min_tshirts"] = num_blue_tshirts + 1
            ans_red_tshirt_first["min_socks"] = 1
        elif num_blue_tshirts == 0:
            ans_red_tshirt_first["min_tshirts"] = 1
            ans_red_tshirt_first["min_socks"] = num_blue_socks + 1
        elif num_blue_socks == 0:
            ans_red_tshirt_first["min_tshirts"] = num_blue_tshirts + 1
            ans_red_tshirt_first["min_socks"] = 1
        elif num_red_socks == 0:
            pass
        else:
            ans_red_tshirt_first["min_tshirts"] = num_blue_tshirts + 1
            ans_red_tshirt_first["min_socks"] = num_blue_socks + 1
        
        tries_to_picks["red_tshirt_first"] = ans_red_tshirt_first
        tries_to_picks["red_tshirt_first"]["sum"] = ans_red_tshirt_first["min_tshirts"] + ans_red_tshirt_first["min_socks"]

    #try to pick blue socks first
    if num_blue_socks != 0:
        ans_blue_socks_first = {"min_tshirts": 0, "min_socks": 0, "sum": 0}
        if num_blue_socks <= num_red_socks:
            ans_blue_socks_first["min_tshirts"] = 1
            ans_blue_socks_first["min_socks"] = num_red_socks + 1
        elif num_red_socks == 0:
            ans_blue_socks_first["min_tshirts"] = num_red_tshirts + 1
            ans_blue_socks_first["min_socks"] = 1
        elif num_red_tshirts == 0:
            ans_blue_socks_first["min_tshirts"] = 1
            ans_blue_socks_first["min_socks"] = num_red_socks + 1
        elif num_blue_tshirts == 0:
            pass
        else:
            ans_blue_socks_first["min_tshirts"] = num_red_tshirts + 1
            ans_blue_socks_first["min_socks"] = num_red_socks + 1

        tries_to_picks["blue_socks_first"] = ans_blue_socks_first
        tries_to_picks["blue_socks_first"]["sum"] = ans_blue_socks_first["min_tshirts"] + ans_blue_socks_first["min_socks"]
    
    #try to pick red socks first
    if num_red_socks != 0:
        ans_red_socks_first = {"min_tshirts": 0, "min_socks": 0, "sum": 0}
        if num_red_socks <= num_blue_socks:
            ans_red_socks_first["min_tshirts"] = 1
            ans_red_socks_first["min_socks"] = num_blue_socks + 1
        elif num_blue_socks == 0:
            ans_red_socks_first["min_tshirts"] = num_blue_tshirts + 1
            ans_red_socks_first["min_socks"] = 1
        elif num_blue_tshirts == 0:
            ans_red_socks_first["min_tshirts"] = 1
            ans_red_socks_first["min_socks"] = num_blue_socks + 1
        elif num_red_tshirts == 0:
            pass
        else:
            ans_red_socks_first["min_tshirts"] = num_blue_tshirts + 1
            ans_red_socks_first["min_socks"] = num_blue_socks + 1
        
        tries_to_picks["red_socks_first"] = ans_red_socks_first
        tries_to_picks["red_socks_first"]["sum"] = ans_red_socks_first["min_tshirts"] + ans_red_socks_first["min_socks"]

    return tries_to_picks

all_pos_tries = check_min_amount_of_clotches(num_blue_tshirts, num_red_tshirts, num_blue_socks, num_red_socks)

min_sum = math.inf
min_elements = None
for key, value in all_pos_tries.items():
    if value and value["sum"] > 0:
        if value["sum"] < min_sum:
            min_sum = value["sum"]
            min_elements = value

ans_tshirt = min_elements["min_tshirts"]
ans_socks = min_elements["min_socks"]

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans_tshirt))
    file.write("\n")
    file.write(str(ans_socks))
