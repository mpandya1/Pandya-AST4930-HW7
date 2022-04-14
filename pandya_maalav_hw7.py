import numpy as np
from astropy import units as u
import matplotlib.pyplot as plt

data = np.loadtxt("sed.txt", delimiter = ",")

wv = data[:, 0] #Wavelength
lm = data[:, 1] #Luminosity

x = np.where((wv > 10) & (wv < 1000))

tempOne  = x[0] #Returns an array
tempTwo = x[-1]

lowerBound = tempOne[0]
upperBound = tempTwo[-1]
integral = np.trapz(np.flip(tempTwo), np.flip(tempOne))

print(lowerBound)
print(upperBound)
print(integral)

plt.plot(wv, lm)
plt.xscale("log")
plt.yscale("log")

plt.show()

plt.savefig('pandya_maalav_hw7.png', dpi = 300)