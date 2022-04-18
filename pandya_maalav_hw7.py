import numpy as np
from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt

# Reading the two columns into two arrays, accounting for the file's header. Then, renaming the columns of data in the file
data = pd.read_csv("sed.txt", sep = ",", header = None, skiprows = 2)
data.columns = ["wv", "lm"]

# print(data)

# Determining where the wavelength values ae correct, and then pulling the upper and lower bound values out via an intermediate array
bounds = np.where((data["wv"] >= 10) & (data["wv"] <= 1000))
boundsArr = bounds[0]
upper = boundsArr[-1]
lower = boundsArr[0]

data["wv"] *= u.micron
data["lm"] *= u.Lsun/u.micron

# print (upper, lower)

#np.loadtxt("sed.txt", delimiter = ",")



# wv = data[:, 0] #Wavelength
# lm = data[:, 1] #Luminosity

# x = np.where((wv > 10) & (wv < 1000))

# tempOne  = x[0] #Returns an array
# tempTwo = x[-1]

# lowerBound = tempOne[0]
# upperBound = tempTwo[-1]
# integral = np.trapz(np.flip(tempTwo), np.flip(tempOne))

# print(lowerBound)
# print(upperBound)
# print(integral)

# Plotting the data
plt.plot(data["wv"], data["lm"])
plt.xscale("log")
plt.yscale("log")

plt.show()

plt.savefig('Test-pandya_maalav_hw7.png', dpi = 300)