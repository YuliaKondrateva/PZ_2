import matplotlib.pyplot as plt

months = ["Сент", "Окт", "Нояб", "Дек"]
subjects = {
    "Мат. Анализ": [4, 5, 5, 4],
    "Химия": [5, 4, 4, 5],
    "Начертательная геометрия": [4, 5, 5, 5],
    "АЯП": [4, 4, 5, 4]
}

plt.figure(figsize=(10, 6))

for subject, grades in subjects.items():
    plt.plot(grades, marker="o", label=subject)

plt.ylabel("Оценки")
plt.title("Задание 3. Вариант 1")
plt.yticks([4, 5])
plt.legend()

plt.show()