import numpy as np
from astropy import units as u
import pandas as pd
import matplotlib.pyplot as plt

# Reading the two columns into two arrays, accounting for the file's header. Then, renaming the columns of data in the file
data = pd.read_csv("sed.txt", sep = ",", header = None, skiprows = 2)
data.columns = ["wv", "lm"]


# Determining where the wavelength values ae correct, and then pulling the upper and lower bound values out via an intermediate array
bounds = np.where((data["wv"] >= 10) & (data["wv"] <= 1000))
boundsArr = bounds[0]
upper = boundsArr[-1]
lower = boundsArr[0]

# Creating two lists containing the values of luminosity and wavelength in between the bounds
wvList = list()
lmList = list()

i = lower
while (i < upper):
    wvList.append(data["wv"][i])
    lmList.append(data["lm"][i])
    i += 1

    
# Defining new arrays with units attached to the values
wvUnits = wvList * u.micron
lmUnits = lmList * u.Lsun/u.micron

# Calculating the integral with the given units
integral = np.trapz(np.flip(lmUnits), np.flip(wvUnits))
print(integral)

# Converting the integral to the desired units
ergIntegral = integral.to(u.erg/u.s)
print(ergIntegral)

# Plotting the data
plt.plot(data["wv"], data["lm"])
plt.xscale("log")
plt.yscale("log")
plt.xlabel("Wavelength")
plt.ylabel("Luminosity")
# plt.xlim(data["wv"].min(), data["wv"].max())
plt.bar(wvList, lmList, color = "red")

plt.show()

plt.savefig('pandya_maalav_hw7.png', dpi = 300)