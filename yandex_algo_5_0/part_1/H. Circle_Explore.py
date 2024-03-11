import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Параметры окружности
r = 1  # Радиус
theta = np.linspace(0, 2 * np.pi, 100)  # Для рисования окружности

# Координаты окружности
x_circle = r * np.cos(theta)
y_circle = r * np.sin(theta)

# Функция для анимации
def update(frame):
    x, y = r * np.cos(frame), r * np.sin(frame)
    x_2, y_2 = r * np.cos(frame), r * np.sin(frame)
    point.set_data(x, y)
    point_2.set_data(x_2, y_2)
    return point, point_2


# Создаем фигуру для анимации
fig, ax = plt.subplots(figsize=(6, 6))

# Рисуем окружность
ax.plot(x_circle, y_circle, label="Окружность")

# Настройки графика
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)
ax.set_aspect("equal", adjustable="box")
ax.grid(color="gray", linestyle="--", linewidth=0.5)
ax.set_title("Движение объекта по окружности")
ax.legend()

# Добавляем точку, которая будет анимирована
(point,) = ax.plot([], [], "ro")
(point_2,) = ax.plot([], [], "ro")

# Создаем анимацию
ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), blit=True)

plt.show()
