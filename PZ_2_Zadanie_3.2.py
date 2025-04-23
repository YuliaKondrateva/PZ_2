import matplotlib.pyplot as plt

years = ["2011", "2016", "2021", "2026"]
parties = ["Единая Россия", "КПРФ", "ЛДПР", "Справедливая Россия", "Другие"]

seats = [
    [238, 92, 56, 64, 0],
    [343, 42, 39, 23, 3],
    [324, 57, 21, 27, 21],
    [315, 50, 30, 35, 20]
]

fig, ax = plt.subplots(figsize=(8, 5))

bottom = [0] * len(years)

for i in range(len(parties)):
    ax.bar(years, [seats[j][i] for j in range(len(years))], bottom=bottom, label=parties[i])
    bottom = [bottom[j] + seats[j][i] for j in range(len(years))]

ax.set_xlabel("Годы выборов", fontsize=12)
ax.set_ylabel("Количество мест", fontsize=12)
ax.set_title("Распределение партий в Государственной Думе", fontsize=14)
ax.legend(title="Партии", bbox_to_anchor=(1.05, 1), loc='upper left')
ax.set_ylim(0, 450)
ax.grid(axis='y', linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
