import numpy as np
from matplotlib.widgets import Slider
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt


def generate():
    base = np.linspace(0, 5, 11)
    # base = np.random.randint(0, 10, 5)
    outliers = np.random.randint(10, 20, 2)
    data = np.concatenate((base, outliers))
    np.random.shuffle(data)
    return data


# Generating the noisy signal
x = np.concatenate((np.array([0]), generate()))  # np.linspace(0, 2*np.pi, 100)
y = np.concatenate((np.array([0]), generate()))  # np.sin(x) + np.cos(x) + np.random.random(100)
print(len(y))
# Savitzky-Golay filter
y_filtered = savgol_filter(y, len(y) - 1, 10)
x_filtered = savgol_filter(x, len(x) - 1, 10)

# Plotting
fig = plt.figure()
ax = fig.subplots()
p = ax.plot(x, y, '*')
p, = ax.plot(x_filtered, y_filtered, 'g')
plt.subplots_adjust(bottom=0.25)

print("X unfiltered>> ", x)
print("Y unfiltered>> ", y)
print("X filtered>> ", x_filtered)
print("Y filtered>> ", y_filtered)
plt.show()

