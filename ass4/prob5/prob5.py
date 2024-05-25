import matplotlib.pyplot as plt
import numpy as np
n=10000

def gaussian(x):
	return 1/np.sqrt(2*np.pi)*np.exp(-x**2/2)
u1=np.random.rand(n)
u2=np.random.rand(n)
x=[np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2) for U1,U2 in zip(u1,u2)]
x_vals=np.linspace(-5,5)
y_vals=gaussian(x_vals)
plt.plot(x_vals,y_vals,label="gaussain pdf")
plt.hist(x,bins=20,density=True,label="histogram (box muller method)")
plt.xlabel("random numbers")
plt.ylabel("density")
plt.legend()
plt.savefig("fig1.png")
