import numpy as np
from matplotlib.widgets import Slider
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt

# Generating the noisy signal
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + np.cos(x) + np.random.random(100)

# Savitzky-Golay filter
y_filtered = savgol_filter(y, 99, 3)

# Plotting
fig = plt.figure()
ax = fig.subplots()
p = ax.plot(x, y, '-*')
p, = ax.plot(x, y_filtered, 'g')
plt.subplots_adjust(bottom=0.25)

# Defining the Slider button
ax_slide = plt.axes([0.25, 0.1, 0.65, 0.03])  # position, yposition, width and height
# Properties of the slider
win_size = Slider(ax_slide, 'Window size', valmin=5, valmax=99, valinit=99, valstep=2)


# Updating the plot
def update(val):
    current_v = int(win_size.val)
    new_y = savgol_filter(y, current_v, 3)
    p.set_ydata(new_y)
    fig.canvas.draw()  # redraw the figure


# calling the function "update" when the value of the slider is changed
win_size.on_changed(update)
plt.show()
