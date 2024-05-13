import numpy as np
import matplotlib.pyplot as plt
import cmath

def f(x):
	return 10;


x_min=-40
x_max=40

n=2**10
x_vals=np.linspace(x_min,x_max,n)
delta=x_vals[1]-x_vals[0]
y_vals=np.array([f(x) for x in x_vals])

y_dft=np.fft.fft(y_vals,norm="ortho")
n=len(y_dft)
k_vals=np.fft.fftshift(2*np.pi*np.fft.fftfreq(n,delta))
y_dft=np.fft.fftshift(y_dft)
yt_vals=np.array([delta*np.sqrt(n/(2*np.pi))*cmath.exp(-1j*x_min*kq)*y_dft[i] for i,kq in enumerate(k_vals)])



plt.plot(k_vals,np.abs(yt_vals),".-c")
plt.xlabel("k")
plt.ylabel(r"$\tilde{f}(k)$")

plt.suptitle("Fourier Transform of Constant Function")

#plt.show()
plt.savefig("fig")

