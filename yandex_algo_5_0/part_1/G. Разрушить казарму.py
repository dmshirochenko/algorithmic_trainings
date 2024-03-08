import math 

# Reading from the file
with open("input.txt", "r") as reader:
    num_of_soldiers = int(reader.readline().strip())
    barracks_health = int(reader.readline().strip())
    enemy_troops_generation_speed = int(reader.readline().strip())

enemy_troops = 0
num_of_rounds = 0
is_game_ends = False
game_result = -1
alt_num_of_rounds = math.inf
min_alt_num_of_rounds = math.inf

while True:
    num_of_rounds += 1

    if num_of_soldiers > enemy_troops:
        force_to_use_on_barracks = min(barracks_health, num_of_soldiers - enemy_troops)
        force_to_use_on_troops = num_of_soldiers - force_to_use_on_barracks
    else:
        if barracks_health > 0:
            force_to_use_on_barracks = 1
        else:
            force_to_use_on_barracks = 0
        force_to_use_on_troops = num_of_soldiers - force_to_use_on_barracks

    if num_of_soldiers > barracks_health:
        alt_num_of_soldiers = num_of_soldiers
        alt_num_of_enemy_troops = enemy_troops
        alt_num_of_rounds = num_of_rounds
        
        alt_force_to_use_on_troops = num_of_soldiers - barracks_health
        alt_num_of_enemy_troops -= alt_force_to_use_on_troops
        alt_num_of_soldiers -=  alt_num_of_enemy_troops
        while True:
            alt_num_of_rounds += 1
            alt_num_of_enemy_troops -= alt_num_of_soldiers
            if alt_num_of_enemy_troops <= 0:
                break
            alt_num_of_soldiers -= alt_num_of_enemy_troops
            if alt_num_of_soldiers <= 0:
                alt_num_of_rounds = math.inf
                break
        
        min_alt_num_of_rounds = min(min_alt_num_of_rounds, alt_num_of_rounds)
        

    if enemy_troops > 0:
        if enemy_troops > force_to_use_on_troops:
            enemy_troops -= force_to_use_on_troops
        else:
            enemy_troops = 0
            
    if barracks_health > 0:
        if barracks_health > force_to_use_on_barracks:
            barracks_health -= force_to_use_on_barracks
        else:
            barracks_health = 0

    num_of_soldiers -= enemy_troops

    if barracks_health > 0:
        enemy_troops += enemy_troops_generation_speed


    if num_of_soldiers <= 0:
        is_game_ends = True

    if barracks_health <= 0 and enemy_troops <= 0:
        game_result = 1
        is_game_ends = True
    
    if is_game_ends:
        break


if  game_result == -1 and min_alt_num_of_rounds == math.inf:
    num_of_rounds = -1
elif game_result == -1 and min_alt_num_of_rounds != math.inf:
    num_of_rounds = min_alt_num_of_rounds
else:
    num_of_rounds = min(num_of_rounds, min_alt_num_of_rounds)

with open("output.txt", "w") as file:
    file.write(str(num_of_rounds))