with open("input.txt", "r") as reader:
    lift_capacity = int(reader.readline())
    num_floors = int(reader.readline())
    people_on_the_floor = []
    for _ in range(num_floors):
        people_on_the_floor.append(int(reader.readline()))

print("lift_capacity= ", lift_capacity)
print("num_floors= ", num_floors)
print("people_on_the_floor= ", people_on_the_floor)


time_to_pass = 0

# print(people_on_the_floor)
num_people_left = 0
for item in people_on_the_floor:
    num_people_left += item

min_floor_to_check = len(people_on_the_floor) - 1
while num_people_left > 0:
    current_lift_capacity = lift_capacity
    highest_floor = True
    for i in range(min_floor_to_check, -1, -1):

        # print("people_on_the_floor[i]", people_on_the_floor[i], " i = ", i )
        if people_on_the_floor[i] != 0:
            if people_on_the_floor[i] == current_lift_capacity:
                # print("people_on_the_floor[i] == current_lift_capacity")
                current_lift_capacity = 0
                if highest_floor:
                    time_to_pass += (i + 1) * 2
                    highest_floor = False
                num_people_left -= people_on_the_floor[i]
                people_on_the_floor[i] = 0
            elif people_on_the_floor[i] > current_lift_capacity:
                # print("people_on_the_floor[i] > current_lift_capacity")
                # print("current_lift_capacity = ", current_lift_capacity)

                if highest_floor:
                    k = people_on_the_floor[i] // current_lift_capacity
                    people_on_the_floor[i] -= k * current_lift_capacity
                    num_people_left -= k * current_lift_capacity
                    current_lift_capacity = 0

                    time_to_pass += k * ((i + 1) * 2)
                    highest_floor = False
                else:
                    people_on_the_floor[i] -= current_lift_capacity
                    num_people_left -= current_lift_capacity
                    current_lift_capacity = 0

                # print("people_on_the_floor", people_on_the_floor[i])
                # print("num_people_left = ", num_people_left)
            elif people_on_the_floor[i] < current_lift_capacity:
                # print("people_on_the_floor[i] < current_lift_capacity")
                # print(people_on_the_floor[i] < current_lift_capacity)
                current_lift_capacity -= people_on_the_floor[i]

                if highest_floor:
                    time_to_pass += (i + 1) * 2
                    highest_floor = False

                num_people_left -= people_on_the_floor[i]
                people_on_the_floor[i] = 0
                # print("num_people_left = ", num_people_left)
                min_floor_to_check = min(min_floor_to_check, i)

        else:
            min_floor_to_check = min_floor_to_check = min(min_floor_to_check, i - 1)

        if current_lift_capacity == 0:
            break


with open("output.txt", "w") as file:
    file.write(str(time_to_pass))
