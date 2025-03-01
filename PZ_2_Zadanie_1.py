import matplotlib.pyplot as plt
x = [_ for _ in range(10)]
y1 = [x for x in range(10)]
y2 = [2*x for x in range(10)]
y3 = [3*x for x in range(10)]
y4 = [x**2 for x in range(10)]
y5 = [2*(x**2) for x in range(10)]

plt.plot(x, y1, color='r', label='y1')
plt.plot(x, y2, color='k', label='y2')
plt.plot(x, y3, color='b', label='y3')
plt.plot(x, y4, color='g', label='y4')
plt.plot(x, y5, color='c', label='y5')
plt.show()