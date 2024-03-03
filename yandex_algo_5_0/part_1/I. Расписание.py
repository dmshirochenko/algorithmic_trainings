# Reading from the file
with open("input.txt", "r") as reader:
    N = int(reader.readline().strip())
    year = int(reader.readline().strip())
    bank_holidays = set()
    for _ in range(N):
        data, month = reader.readline().strip().split(" ")
        bank_holidays.add((int(data), month))

    day_of_the_week_first_of_january = reader.readline().strip()

days_of_week_lst = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

months_dict = {
    "January": {"ru": "Январь", "days": 31},
    "February": {"ru": "Февраль", "days": 28},
    "March": {"ru": "Март", "days": 31},
    "April": {"ru": "Апрель", "days": 30},
    "May": {"ru": "Май", "days": 31},
    "June": {"ru": "Июнь", "days": 30},
    "July": {"ru": "Июль", "days": 31},
    "August": {"ru": "Август", "days": 31},
    "September": {"ru": "Сентябрь", "days": 30},
    "October": {"ru": "Октябрь", "days": 31},
    "November": {"ru": "Ноябрь", "days": 30},
    "December": {"ru": "Декабрь", "days": 31},
}


def is_leap_year(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


is_current_year_leap = is_leap_year(year)
if is_current_year_leap:
    months_dict["February"]["days"] = 29


def day_shift(days_of_week_lst, day_of_the_week):
    for index, day in enumerate(days_of_week_lst):
        if day == day_of_the_week:
            return index


def counter_init(days_of_week_lst):
    dct = {}
    for day in days_of_week_lst:
        dct[day] = 0
    return dct


year_week_day_shift = day_shift(days_of_week_lst, day_of_the_week_first_of_january)
day_counter = counter_init(days_of_week_lst)

for month in months_dict:
    current_day_index = 0
    last_day_of_the_month = False
    max_day_current_month = months_dict[month]["days"]
    while not last_day_of_the_month:
        for i in range(year_week_day_shift, len(days_of_week_lst)):
            current_day_index += 1
            if (current_day_index, month) not in bank_holidays:
                day_counter[days_of_week_lst[i]] += 1
            if current_day_index == max_day_current_month:
                last_day_of_the_month = True
                break

        if not last_day_of_the_month:
            for i in range(0, year_week_day_shift):
                current_day_index += 1
                if (current_day_index, month) not in bank_holidays:
                    day_counter[days_of_week_lst[i]] += 1
                if current_day_index == max_day_current_month:
                    last_day_of_the_month = True
                    break

        year_week_day_shift = i + 1

min_day = min(day_counter, key=day_counter.get)

max_day = max(day_counter, key=day_counter.get)

ans = max_day + " " + min_day
# Writing to the file
with open("output.txt", "w") as file:
    file.write(ans)
