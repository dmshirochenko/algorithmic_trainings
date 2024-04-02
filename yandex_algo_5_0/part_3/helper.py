import matplotlib.pyplot as plt

# Coordinates of the points
points = [
    (8, 6),
    (-9, 6),
    (-4, 1),
    (-5, 3),
    (6, 4),
    (7, -2),
    (9, 2),
    (9, 8),
    (8, 10),
    (-7, -2),
    (-5, -6),
    (1, 7),
    (3, 10),
]

# Unpack points into x and y coordinates
x_coords, y_coords = zip(*points)

# Plotting
plt.figure(figsize=(8, 8))
plt.scatter(x_coords, y_coords, color="blue")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.axhline(y=0, color="k")
plt.axvline(x=0, color="k")
plt.title("Graph of the Points")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# Setting equal aspect ratio to ensure the square's sides appear correctly
plt.axis("equal")

plt.show()
