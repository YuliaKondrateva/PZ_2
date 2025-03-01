import random as r
import matplotlib.pyplot as plt

num_groups = 5
points_per_group = 10

x_range = (0, 10)
y_range = (0, 10)

groups = []

for _ in range(num_groups):
    center_x = r.uniform(*x_range)
    center_y = r.uniform(*y_range)

    points = []
    for _ in range(points_per_group):
        dx = r.uniform(-1, 1)
        dy = r.uniform(-1, 1)
        points.append((center_x + dx, center_y + dy))
    
    groups.append((center_x, center_y, points))

plt.figure(figsize=(8, 6))

for center_x, center_y, points in groups:

    x_vals, y_vals = zip(*points)

    avg_x = sum(x_vals) / len(x_vals)
    avg_y = sum(y_vals) / len(y_vals)

    max_dev_x = max(abs(x - avg_x) for x in x_vals)
    max_dev_y = max(abs(y - avg_y) for y in y_vals)

    plt.scatter(x_vals, y_vals, alpha=0.5)
    plt.scatter(avg_x, avg_y, color="red", marker="o", s=100)
    plt.errorbar(avg_x, avg_y, xerr=max_dev_x, yerr=max_dev_y, fmt='o', color='red', capsize=5)

plt.xlabel("Ось X")
plt.ylabel("ось Y")
plt.title("Задание 2")
plt.show()