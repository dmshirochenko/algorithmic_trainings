# Reading from the file
with open("input.txt", "r") as reader:
    income, founders, days = map(int, reader.readline().split(" "))

#import sys
#sys.set_int_max_str_digits(0)

DIGITS_TO_TRY = [str(i) for i in range(10)]

for digit in DIGITS_TO_TRY:
    new_income = str(income) + digit
    if int(new_income) % founders == 0:
        income = int(new_income)
        break
else:
    income = -1

if income != -1:
    zeros = '0' * (days - 1)

# Writing to the file
with open("output.txt", "w") as file:
    if income == -1:
        file.write(str(income))
    else:
        file.write(str(income) + zeros)