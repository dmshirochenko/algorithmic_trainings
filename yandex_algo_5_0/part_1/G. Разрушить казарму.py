# Reading from the file
with open("input.txt", "r") as reader:
    num_of_soldiers = int(reader.readline().strip())
    barracks_health = int(reader.readline().strip())
    enemy_troops_generation_speed = int(reader.readline().strip())

num_of_rounds = 0
enemy_troops = 0
solders_left = num_of_soldiers
enemy_troops_left = 0
barracks_health_left = barracks_health
current_round = 1
min_round = -1
game_round_results = []

while True:
    print("Rounds starts  ", current_round)
    each_round_conditions = []
    print("New num_of_soldiers", solders_left)
    num_of_soldiers = solders_left
    for i in range(num_of_soldiers + 1):
        current_num_of_solders = num_of_soldiers
        enemy_troops = enemy_troops_left
        barracks_health = barracks_health_left
        innner_round = current_round

        force_to_use_on_troops = i
        force_to_use_on_barracks = current_num_of_solders - i
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

        current_num_of_solders -= enemy_troops

        if barracks_health > 0:
            enemy_troops += enemy_troops_generation_speed

        each_round_conditions.append((current_num_of_solders, barracks_health, enemy_troops, innner_round + 1))


    for round in each_round_conditions:
        is_game_ends = False
        solders_left, barracks_health_left, enemy_troops_left, current_round = round
        print('Before final check =', solders_left, barracks_health_left, enemy_troops_left)
        
        if solders_left <= 0:
            game_round_results.append(('lose', current_num_of_solders, barracks_health, current_round))
            is_game_ends = True

        if barracks_health <= 0 and enemy_troops <= 0:
            game_round_results.append(('win', current_num_of_solders, barracks_health, current_round))
            is_game_ends = True

    
print(game_round_results)

print(num_of_rounds)
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(num_of_rounds))