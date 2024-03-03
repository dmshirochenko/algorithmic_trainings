# Reading from the file
with open("input.txt", "r") as reader:
    score_game_one_team_first, score_game_one_team_second = map(int, reader.readline().rstrip().split(":"))
    score_game_second_team_first, score_game_second_team_second = map(int, reader.readline().rstrip().split(":"))
    home_away = int(reader.readline())

goals_first_team = (score_game_one_team_first, score_game_second_team_first)
goals_second_team = (score_game_one_team_second, score_game_second_team_second)

ans = 0
goal_diff = sum(goals_second_team) - sum(goals_first_team)

if goal_diff == 0:
    if sum(goals_first_team) == 0:
        ans = 1
    elif home_away == 1:
        if goals_second_team[0] >= goals_first_team[1]:
            ans = 1
    elif home_away == 2:
        if goals_second_team[1] >= goals_first_team[0]:
            ans = 1
elif goal_diff > 0:
    if home_away == 1:
        if (goal_diff + goals_first_team[1]) > goals_second_team[0]:
            ans = goal_diff
        else:
            ans = goal_diff + 1
    elif home_away == 2:
        if goals_first_team[0] > goals_second_team[1]:
            ans = goal_diff
        else:
            ans = goal_diff + 1


# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
