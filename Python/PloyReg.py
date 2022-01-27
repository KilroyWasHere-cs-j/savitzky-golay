import operator
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures

outputX = []
outputY = []
np.random.seed(0)
# Robot Movements
x = np.array([1, 2, 2, 2, 6, 6.7, 45])
print(x.shape)
y = np.array([2, 3, 4, 6.7, 1, 14, 23])
print(y.shape)
# transforming the data to include another axis
x = x[:, np.newaxis]
y = y[:, np.newaxis]
degree = 4
polynomial_features = PolynomialFeatures(degree=int(degree))
x_poly = polynomial_features.fit_transform(x)

model = LinearRegression()
model.fit(x_poly, y)
y_poly_pred = model.predict(x_poly)

rmse = np.sqrt(mean_squared_error(y, y_poly_pred))
r2 = r2_score(y, y_poly_pred)
print("RMSE:" + str(rmse))
print("R2: " + str(r2))

plt.scatter(x, y, s=10)
# sort the values of x before line plot
sort_axis = operator.itemgetter(0)
sorted_zip = sorted(zip(x, y_poly_pred), key=sort_axis)
x, y_poly_pred = zip(*sorted_zip)
plt.plot(x, y_poly_pred, color='m')
for i in x:
    outputX.append(float(i))
for x in y_poly_pred:
    outputY.append(float(x))
print("X: ", outputX)
print("Y: ", outputY)
plt.show()
