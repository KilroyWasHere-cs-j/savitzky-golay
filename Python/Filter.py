import numpy as np
from scipy.signal import savgol_filter
import matplotlib.pyplot as plt
import MadDog

x = []
y = []


def generate():
    # Generate random data
    base = np.linspace(0, 5, 11)
    # base = np.random.randint(0, 10, 5)
    outliers = np.random.randint(10, 20, 2)
    data = np.concatenate((base, outliers))
    np.random.shuffle(data)
    return data


def fill_data():
    # Build random data
    return np.concatenate((np.array([0]), MadDog.find_outliers(generate()))), np.concatenate(
        (np.array([0]), MadDog.find_outliers(generate())))  # np.sin(x) + np.cos(x) + np.random.random(100)
    # np.linspace(0, 2*np.pi, 100)


def savitzky(x, y, ploy_nom):
    return savgol_filter(x, len(x) - 1, 10), savgol_filter(y, len(y) - 1, 10)


def map(x_filtered, y_filtered, x, y, title="title"):
    # Generate some test data

    heatmap, xedges, yedges = np.histogram2d(x, y, bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.show()

    heatmap, xedges, yedges = np.histogram2d(x_filtered, y_filtered, bins=50)
    extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

    plt.clf()
    plt.imshow(heatmap.T, extent=extent, origin='lower')
    plt.show()


def show(x_filtered, y_filtered, x, y, title="Lorem ipsum"):
    # Plotting
    fig = plt.figure()
    ax = fig.subplots()
    plt.plot(x_filtered, y_filtered, 'red', marker="o")
    plt.plot(x, y, 'green', marker="o")
    plt.subplots_adjust(bottom=0.25)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.legend(["Filter", "Raw"])
    plt.show()


# Generating the noisy signal
x, y = fill_data()
print(len(y))
# Savitzky-Golay filter
x_filtered, y_filtered = savitzky(x, y, 2)
print("X unfiltered>> ", x)
print("Y unfiltered>> ", y)
print("X filtered>> ", x_filtered)
print("Y filtered>> ", y_filtered)
show(x_filtered, y_filtered, x, y)
