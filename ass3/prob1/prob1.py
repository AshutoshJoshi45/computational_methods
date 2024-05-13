import numpy as np
import matplotlib.pyplot as plt
import cmath

def f(x):
	if x==0:
		return 1;
	else:
		return np.sin(x)/x;


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

#Analytical result using mathematica
def sign(x):
	if x>0:
		return 1;
	if x<0:
		return -1;
	if x==0:
		return 0;
		
def ft(k):
	return 1/2*np.sqrt(np.pi/2)*(sign(1-k)+sign(1+k))
	
#Using results from gsl(prob3)

data=np.loadtxt("prob3results.txt")
y_dftgsl=[complex(a[0],a[1])for a in data]
y_dftgsl=np.fft.fftshift(y_dftgsl)

ytgsl_vals=np.array([delta*np.sqrt(n/(2*np.pi))*cmath.exp(-1j*x_min*kq)*y_dftgsl[i] for i,kq in enumerate(k_vals)])

#Using data from fftw(prob2)
data=np.loadtxt("prob2results.txt")
y_dftfftw=[complex(a[0],a[1]) for a in data]
y_dftfftw=np.fft.fftshift(y_dftfftw)
yt_valsfftw=np.array([delta*np.sqrt(n/(2*np.pi))*cmath.exp(-1j*x_min*kq)*y_dftfftw[i] for i,kq in enumerate(k_vals)])


plt.subplot(3,1,1)
plt.plot(k_vals,np.abs(yt_vals),"--c")
plt.plot(k_vals,[ft(k) for k in k_vals],"--r")
plt.legend(["numpy.fft.fft","true soln"])
plt.ylabel(r"$\tilde{f}(k)$")
plt.xlim(-10,10)

plt.subplot(3,1,2)
plt.plot(k_vals,np.abs(yt_valsfftw),"--c")
plt.plot(k_vals,[ft(k) for k in k_vals],"--r")
plt.legend(["fftw3","true soln"])
plt.ylabel(r"$\tilde{f}(k)$")
plt.xlim(-10,10)

plt.subplot(3,1,3)
plt.plot(k_vals,np.abs(ytgsl_vals),"--c")
plt.plot(k_vals,[ft(k) for k in k_vals],"--r")
plt.legend(["gsl","true soln"])
plt.ylabel(r"$\tilde{f}(k)$")
plt.xlabel("k")
plt.xlim(-10,10)

plt.suptitle("Fourier Transform of Sinc Function")

#plt.show()
plt.savefig("fig2")

