from scipy.fftpack import fft, fftfreq, ifft
import matplotlib.pyplot as plt
import numpy             as np
import math
T = [1800, 1500, 1200, 1000, 800, 750, 700]
gr = [[]] * len(T)
w = np.loadtxt('omega.dat' , usecols=[0], unpack=True) 
i = 0
for n in T:
	gr[i] = np.loadtxt('gr_%i.dat' %(n), usecols=[0], unpack=True)
	plt.plot(w,gr[i], label = '%i' %(n))
        i += 1
plt.axis([0, 50, 0.0001, 0.5])
plt.xlabel('$\omega$ (THz)')
plt.ylabel('$g(\omega)/\omega^2$')
plt.legend()
plt.show()
