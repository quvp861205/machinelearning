import numpy as np
import matplotlib.pyplot as plt
import random


x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
y = np.array([random.randint(-5, 20) for i in range(len(x))])

coeffs = np.polyfit(x, y, 1)
print(coeffs)

m = coeffs[0]
b = coeffs[1]

est_y = (m * x) + b

plt.plot(x, est_y)
plt.scatter(x, y)
plt.show()