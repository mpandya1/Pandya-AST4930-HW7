import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

data = np.loadtxt("sed.txt", delimiter = ",")

x = data[:, 0]
y = data[:, 1]

plt.plot(x, y)
plt.xscale("log")
plt.yscale("log")

plt.show()

plt.savefig('pandya_maalav_hw7.png', dpi = 300)