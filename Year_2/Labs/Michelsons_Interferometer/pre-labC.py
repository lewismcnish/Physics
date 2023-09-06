import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import os
import scipy.optimize as opt

title_size = 18
axis_size = 14


def intensity(d, lam):
    return np.sin(2*np.pi*d/(lam))**2


lam = 530e-9

d= np.linspace(1e-6, 5e-6, 1000)

plt.figure()
plt.plot(d, intensity(d, lam))
plt.title('Intensity vs. Distance', fontsize=title_size)
plt.xlabel(r'Distance ($\mu$m)', fontsize=axis_size)
plt.ylabel('Intensity (arb. units)', fontsize=axis_size)
plt.show()

lam2 = 535e-9
d2 = np.linspace(1e-6, 50e-6, 10000000)
def totIntensity(d, lam1, lam2):
    return intensity(d, lam1) + intensity(d, lam2)

plt.figure()
plt.plot(d2, totIntensity(d2, lam, lam2))
plt.title('Total Intensity vs. Distance', fontsize=title_size)
plt.xlabel(r'Distance ($\mu$m)', fontsize=axis_size)
plt.xticks(np.arange(0, 50e-6, 5e-6))
plt.ylabel('Intensity (arb. units)', fontsize=axis_size)
plt.show()