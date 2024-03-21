import re


def read_lines(file_path):
    with open(file_path, "r") as reader:
        for line in reader:
            yield line.strip()


def team_total_goals(team_stat, player_stat, data_input):
    team_to_check = data_input[0]
    if team_to_check in team_stat:
        return len(team_stat[team_to_check]["goals"])


def team_mean_goals(team_stat, player_stat, data_input):
    team_to_check = data_input[0]
    if team_to_check in team_stat:
        mean_goals = len(team_stat[team_to_check]["goals"]) / team_stat[team_to_check]["total_num_of_matches"]
        return mean_goals


def team_first_goals(team_stat, player_stat, data_input):
    team_to_check = data_input[0]
    if team_to_check in team_stat:
        num_of_first_goals = 0
        for goal in team_stat[team_to_check]["goals"]:
            is_first_goal, minute, player = goal
            if is_first_goal:
                num_of_first_goals += 1

        return num_of_first_goals


def player_total_goals(team_stat, player_stat, data_input):
    player_to_check = data_input[0]
    if player_to_check in player_stat:
        return len(player_stat[player_to_check]["goals"])


def player_mean_goals(team_stat, player_stat, data_input):
    player_to_check = data_input[0]
    if player_to_check in player_stat:
        player_team = player_stat[player_to_check]["team"]
        mean_goals = len(player_stat[player_to_check]["goals"]) / team_stat[player_team]["total_num_of_matches"]
        return mean_goals


def player_scored_on_minute(team_stat, player_stat, data_input):
    on_minute = data_input[0]
    player_to_check = data_input[1]
    count_goals_on_minute = 0
    if player_to_check in player_stat:
        for goal in player_stat[player_to_check]["goals"]:
            is_first_goal, minute = goal
            if minute == on_minute:
                count_goals_on_minute += 1
        return count_goals_on_minute


def player_scored_till_certain_minute(team_stat, player_stat, data_input):
    till_minute = data_input[0]
    player_to_check = data_input[1]
    count_goals_till_minute = 0
    if player_to_check in player_stat:
        for goal in player_stat[player_to_check]["goals"]:
            is_first_goal, minute = goal
            if int(till_minute) >= int(minute):
                count_goals_till_minute += 1
        return count_goals_till_minute


def player_scored_from_certain_minute(team_stat, player_stat, data_input):
    from_minute = 91 - int(data_input[0])
    player_to_check = data_input[1]
    count_goals_from_minute = 0
    if player_to_check in player_stat:
        for goal in player_stat[player_to_check]["goals"]:
            is_first_goal, minute = goal
            if from_minute <= int(minute):
                count_goals_from_minute += 1
        return count_goals_from_minute


def player_first_goals(team_stat, player_stat, data_input):
    player_to_check = data_input[0]
    count_first_goals = 0
    if player_to_check in player_stat:
        for goal in player_stat[player_to_check]["goals"]:
            is_first_goal, minute = goal
            if is_first_goal:
                count_first_goals += 1
        return count_first_goals


def get_first_goal(goals_lst_team_1, goals_lst_team_2):
    if goals_lst_team_1 and goals_lst_team_2:
        if int(goals_lst_team_1[0][2]) > int(goals_lst_team_2[0][2]):
            first_goal = goals_lst_team_2[0]
        else:
            first_goal = goals_lst_team_1[0]
    elif goals_lst_team_1:
        first_goal = goals_lst_team_1[0]
    elif goals_lst_team_2:
        first_goal = goals_lst_team_2[0]
    else:
        first_goal = None

    return first_goal


commands_dct = {
    "Total goals for": (team_total_goals, 'Total goals for "([^"]+)"'),
    "Mean goals per game for": (team_mean_goals, 'Mean goals per game for "([^"]+)"'),
    'Score opens by "': (team_first_goals, 'Score opens by "([^"]+)"'),
    "Total goals by": (player_total_goals, "Total goals by (.+)"),
    "Mean goals per game by": (player_mean_goals, "Mean goals per game by (.+)"),
    "Goals on minute": (player_scored_on_minute, "Goals on minute (.+) by (.+)"),
    "Goals on first": (player_scored_till_certain_minute, "Goals on first (.+) minutes by (.+)"),
    "Goals on last": (player_scored_from_certain_minute, "Goals on last (.+) minutes by (.+)"),
    "Score opens by": (player_first_goals, "Score opens by (.+)"),
}


team_stat = dict()
player_stat = dict()
current_game = dict()

ans = ""
for line in read_lines("input.txt"):
    is_command = False
    # check if it's command

    for command in commands_dct:
        if command == line[: len(command)]:
            func, command_pattern = commands_dct[command]
            command_match = re.search(command_pattern, line)
            func_parameters = []
            for i, group in enumerate(command_match.groups(), start=1):
                func_parameters.append(group)

            result = func(team_stat, player_stat, func_parameters)

            if result is not None:
                ans += str(result) + "\n"
            else:
                ans += "0" + "\n"
            is_command = True
            break

    if not is_command:
        # check if match score
        match_score_pattern = r'"([^"]+)"\s*-\s*"([^"]+)"\s*(\d+):(\d+)'
        match_score = re.search(match_score_pattern, line)
        if match_score:
            team_1 = match_score.group(1)
            team_2 = match_score.group(2)
            score_1 = match_score.group(3)
            score_2 = match_score.group(4)
            current_game["team_1"] = {"team_name": team_1, "goals_left": int(score_1), "goals": []}
            current_game["team_2"] = {"team_name": team_2, "goals_left": int(score_2), "goals": []}

            if team_1 not in team_stat:
                team_stat[team_1] = {"total_num_of_matches": 0, "goals": []}
            if team_2 not in team_stat:
                team_stat[team_2] = {"total_num_of_matches": 0, "goals": []}

            team_stat[team_1]["total_num_of_matches"] += 1
            team_stat[team_2]["total_num_of_matches"] += 1

            continue

        minute_player_scored_pattern = r"([A-Za-z\s]+)\s+(\d+)'"
        match_minute_player_scored = re.search(minute_player_scored_pattern, line)
        if match_minute_player_scored:
            player_name = match_minute_player_scored.group(1)
            minute_mark = match_minute_player_scored.group(2)

            if current_game["team_1"]["goals_left"] > 0:
                if player_name not in player_stat:
                    player_stat[player_name] = {"team": current_game["team_1"]["team_name"], "goals": []}

                current_game["team_1"]["goals"].append((current_game["team_1"]["team_name"], player_name, minute_mark))
                current_game["team_1"]["goals_left"] -= 1

            elif current_game["team_2"]["goals_left"] > 0:
                if player_name not in player_stat:
                    player_stat[player_name] = {"team": current_game["team_2"]["team_name"], "goals": []}

                current_game["team_2"]["goals"].append((current_game["team_2"]["team_name"], player_name, minute_mark))
                current_game["team_2"]["goals_left"] -= 1
            if current_game["team_1"]["goals_left"] == 0 and current_game["team_2"]["goals_left"] == 0:
                first_goal = get_first_goal(current_game["team_1"]["goals"], current_game["team_2"]["goals"])
                # record goals
                for goal in current_game["team_1"]["goals"] + current_game["team_2"]["goals"]:
                    if goal == first_goal:
                        continue

                    team, player, minuite = goal
                    team_stat[team]["goals"].append((False, minuite, player))
                    player_stat[player]["goals"].append((False, minuite))
                else:
                    team, player, minuite = first_goal
                    team_stat[team]["goals"].append((True, minuite, player))
                    player_stat[player]["goals"].append((True, minuite))

                current_game = {}

with open("output.txt", "w") as file:
    file.write(str(ans))
