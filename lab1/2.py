import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = x

plt.title("Линейная зависимость y = x", "r--")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.plot(x, y)
plt.show()
