import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

#la funcion esta dada de la siguiente manera
#$\lambda = sin(\frac{1}{2}x^{2} - \frac{1}{4}y^{2} + 3) cos(2x +1 - e^{y})$
#$f(x) = (x+c)^{p}*m + i$


#Funcion derivable

function = lambda th: np.sin(1/2 * th[0]**2 - 1/4 * th[1]**2 + 3)*np.cos(2*th[0] + 1 - np.e**th[1])
resolution = 100

_x = np.linspace(-2, 2, resolution)
_y = np.linspace(-2, 2, resolution)
_z = np.zeros((resolution, resolution))

for index_x, x in enumerate(_x):
  for index_y, y in enumerate(_y):
    _z[index_y, index_x] = function([x, y])

plt.contourf(_x, _y, _z, 100)
plt.colorbar()

theta = np.random.rand(2) * 4 - 2
_t = np.copy(theta)

increase = 0.001
learing_rate = 0.01

plt.plot(theta[0], theta[1], "o", c="white")

gradient = np.zeros(2)

for _ in range(10000):
  for index_theta, th in enumerate(theta):
      _t = np.copy(theta)

      _t[index_theta] = _t[index_theta] + increase

      derived = (function(_t) - function(theta)) / increase

      gradient[index_theta] = derived

  theta = theta - gradient * learing_rate

  if (_ % 10 == 0):
    plt.plot(theta[0], theta[1], ".", c="red")


plt.plot(theta[0], theta[1], "o", c="yellow")
plt.show()