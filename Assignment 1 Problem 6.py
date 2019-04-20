import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
X = [0, 0.25, 1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 15.0, 20.0, 30.0]
Y = [0.0001, 0.008, 0.012, 0.014, 0.015, 0.02, 0.026, 0.032, 0.036,
0.0358, 0.037]
xMissing = np.linspace(0, 30, 360)
# Attempt to find f(x) for x from [0,30] with 360/30 points
# print(xMissing)
plt.plot(X, Y, 'o')
plt.title("Data Points")
plt.xlabel('X-values')
plt.ylabel('Y-values')
# Linear interpolate
linear_function = interpolate.interp1d(X, Y)
plt.title("Linear Interpolate")
plt.xlabel('X-values')
plt.ylabel('Y-values')
yMissing = linear_function(xMissing)
plt.plot(X, Y, 'o')
plt.plot(xMissing, yMissing, '-')
# Log interpolate
log_linear = interpolate.interp1d(X, np.log(Y))
plt.title("Exp Interpolate")
plt.xlabel('X-values')
plt.ylabel('Y-values')
yMissing = log_linear(xMissing)
plt.plot(X, Y, 'o')
plt.plot(xMissing, np.exp(yMissing), '-')
# Polynomial
# Try to fit an 11th degree polynomial into 11 points
deg = len(X)
polyfit = np.polyfit(X,Y, deg)
p_function = np.poly1d(polyfit)
yMissing = p_function(xMissing)
plt.title("Polynomial Interpolate")
plt.xlabel('X-values')
plt.ylabel('Y-values')
plt.plot(X, Y, 'o')
plt.plot(xMissing, yMissing, '-')
# cubic splines
from scipy.interpolate import CubicSpline
cSpline = CubicSpline(X, Y)
yMissing = cSpline(xMissing)

plt.title("Cubic Splines Interpolate")
plt.xlabel('X-values')
plt.ylabel('Y-values')
plt.plot(X, Y, 'o')
plt.plot(xMissing, yMissing, '-')
