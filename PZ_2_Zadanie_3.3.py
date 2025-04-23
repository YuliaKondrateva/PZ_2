import numpy as np
import matplotlib.pyplot as plt

NUM_ROWS = 11
INITIAL_RADIUS = 25
RADIUS_INCREMENT = 5

radii = [INITIAL_RADIUS + i * RADIUS_INCREMENT for i in range(NUM_ROWS)]
arc_lengths = [r * np.pi for r in radii]
total_arc_length = sum(arc_lengths)

TOTAL_SEATS = 450

seats_per_row = [int(TOTAL_SEATS * (L / total_arc_length)) for L in arc_lengths]
seats_per_row[-1] += TOTAL_SEATS - sum(seats_per_row)

points = []
for radius, count in zip(radii, seats_per_row):
    angles = np.linspace(0, np.pi, count)
    x_vals = radius * np.cos(angles)
    y_vals = radius * np.sin(angles)
    for x, y, angle in zip(x_vals, y_vals, angles):
        points.append((angle, x, y))

points.sort(key=lambda p: p[0], reverse=True)

parties = [
    ("КПРФ", 57, "red"),
    ("Справедливая Россия - За Правду", 27, "orange"),
    ("Единая Россия", 324, "darkblue"),
    ("Новые люди", 13, "lightblue"),
    ("ЛДПР", 21, "royalblue"),
    ("Партия Родина", 1,  "darkred"),
    ("Гражданская Платформа", 1, "purple"),
    ("Партия Роста", 1, "cyan"),
    ("Независимые депутаты", 5,  "gray")
]

fig, ax = plt.subplots(figsize=(9, 6))
ax.set_aspect('equal')
ax.axis('off')

idx = 0

for name, seats, color in parties:
    party_points = points[idx: idx + seats]
    idx += seats
    x_coords = [p[1] for p in party_points]
    y_coords = [p[2] for p in party_points]
    ax.scatter(x_coords, y_coords, s=100, color=color, label=f"{name} ({seats})")

ax.text(0, -5, str(TOTAL_SEATS), fontsize=40, fontweight='bold', ha='center')
ax.legend(loc='upper center', fontsize=12, bbox_to_anchor=(0.5, -0.1), ncol=2)
fig.subplots_adjust(bottom=0.2)

plt.show()
