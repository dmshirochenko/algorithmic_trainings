# Reading from the file
with open("input.txt", "r") as reader:
    x_south_west = int(reader.readline())
    y_south_west = int(reader.readline())
    x_north_east = int(reader.readline())
    y_north_east = int(reader.readline())
    x_swimmer = int(reader.readline())
    y_smimmer = int(reader.readline())

#find other 2 points of rectangle
x_north_west = x_south_west
y_north_west = y_north_east

x_south_east = x_north_east
y_south_east = y_south_west

#define points as tuples
south_west = (x_south_west, y_south_west)
north_east = (x_north_east, y_north_east)
north_west = (x_north_west, y_north_west)
south_east = (x_south_east, y_south_east)

#define which rectangle swimmer is in NE, SE, SW, NW, N, S, E, W
#if it's in nothwest rectangle 
if x_swimmer <= x_north_west and y_smimmer >= y_north_west:
    ans = "NW"
elif x_swimmer >= x_north_east and y_smimmer >= y_north_east:
    ans = "NE"
elif x_swimmer >= x_south_east and y_smimmer <= y_south_east:
    ans = "SE"
elif x_swimmer <= x_south_west and y_smimmer <= y_south_west:
    ans = "SW"
elif x_swimmer <= x_north_west and y_smimmer < y_north_west and y_smimmer > y_south_west:
    ans = "W"
elif x_swimmer > x_north_west and x_swimmer < x_north_east and y_smimmer >= y_north_east:
    ans = "N"
elif x_swimmer >= x_north_east and y_smimmer < y_north_east and y_smimmer > y_south_east:
    ans = "E"
elif x_swimmer > x_south_west and x_swimmer < x_south_east and y_smimmer <= y_south_east:
    ans = "S"

# Writing to the file
with open("output.txt", "w") as file:
    file.write(str(ans))
