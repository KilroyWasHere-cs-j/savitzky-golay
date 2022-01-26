import numpy as np
import matplotlib.pyplot as plt


q = np.linspace(-5, 5, 100)
h = np.sin(4+q)

plt.plot(h)
plt.show()
