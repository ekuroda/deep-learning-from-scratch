import numpy as np
import matplotlib.pylab as plt


def numerical_diff(f, x):
    h = 1e-4
    return (f(x+h) - f(x-h)) / (2*h)

def function_1(x):
    return 0.1*x**2 + 0.2*x - 10

def tangent_line(f, x):
    d = numerical_diff(f, x) # 微分=接戦の傾き
    print(d)
    y = f(x) - d*x # 切片
    return lambda t: d*t + y


x = np.arange(0.0, 20.0, 0.1)
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")

tf = tangent_line(function_1, 8)
y2 = tf(x)

plt.plot(x, y)
plt.plot(x, y2)
plt.show()
