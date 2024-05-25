import numpy as np
import matplotlib.pyplot as plt

import time

def lcg(a, c, m, X0, n):
	X=[X0]
	for i in range(n):
		X.append((a*X[-1]+c)%m)
	return X

def uniform(X):
	out=[]
	for x in X:
		if x<=1 and x>=0:
			out.append(1);
		else:
			out.append(0);
	return out
n=10000
#initialising parameters acc to Numerical Recipes (Chapter 7.1)
m=2e32 #modulus
a=1664525 #multiplier
c=1013904223 #increment
X0=478 #seed

start=time.time()
x=lcg(a,c,m,X0,n)
stop=time.time()-start
print("Time taken=%f secs"%stop)

x=[i/m for i in x]
plt.plot(np.linspace(0,1),uniform(np.linspace(0,1)),"k")
plt.hist(x,bins=20,density=True,color="cyan")
plt.legend(["uniform distribution","random numbers density"])
plt.xlabel("random numbers")
plt.ylabel("density")
plt.savefig("fig1.png")
#plt.show()
