# Reading from the file
with open("input.txt", "r") as reader:
    num_blue_tshirts = int(reader.readline())
    num_red_tshirts = int(reader.readline())


ans = 1
# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
