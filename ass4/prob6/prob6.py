import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return np.sqrt(2/np.pi)*np.exp(-x**2/2)

n=10000
x=np.random.rand(n)*4
y=np.random.rand(n)
x_vals=np.linspace(0,4)
y_good=[]
x_good=[]

for i in range(len(x)):
	if y[i]<=f(x[i]):
		y_good.append(y[i])
		x_good.append(x[i])


plt.hist(x_good,bins=20,density=True,label="histogram (rejection method)")
plt.plot(x_vals,f(x_vals),"k",label="probability density f(x)")
plt.xlabel("random numbers")
plt.ylabel("density")
plt.legend()
plt.savefig("fig1")
