import numpy as np
import matplotlib.pyplot as plt

# costFunc = -(y*lg(y') + (1-y)*log(1-y'))
# When y = 0, costFunc = -log(1-y')
# When y = 1, costFunc = -log(y')

x = np.arange(0.0001, 1.0, 0.0001)
y1 = -np.log(1-x)
y2 = -np.log(x)

plt.plot(x, y1)
plt.text(0.6, 6, 'y = 0, cost = -lg(1-y_hat)')
plt.show()

plt.plot(x, y2)
plt.text(0.6, 1.5, 'y = 1, cost = -lg(y_hat)')
plt.show()
