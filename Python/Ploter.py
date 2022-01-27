import numpy as np
import matplotlib.pyplot as plt


q = np.linspace(0, 5, 100)
print(q)
h = np.sin(4+q)

plt.plot(h)
plt.show()
