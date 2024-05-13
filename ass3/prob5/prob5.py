import numpy as np
import time
import cmath
import matplotlib.pyplot as plt

n_range=np.arange(4,101)

def dft(xn):
	start=time.time()
	Xk=[]
	for k in range(len(xn)):
		summ=0
		for n in range(len(xn)):
			summ=summ+xn[n]*np.exp(-1j*2*np.pi*k*n/len(xn))
		Xk.append(summ)
	return time.time()-start

def fft(xn):
	start=time.time()
	Xk=np.fft.fft(xn)
	return time.time()-start

t_dft=[]
t_fft=[]
	
for n in n_range:
	arr=np.arange(n)
	t_dft.append(dft(arr))
	t_fft.append(fft(arr))

plt.plot(n_range,t_dft,".-c",n_range,t_fft,".-r")
plt.legend(["DFT","FFT"])
plt.xlabel("N")
plt.ylabel("Time(s)")
#plt.show()
plt.savefig("fig")
	
