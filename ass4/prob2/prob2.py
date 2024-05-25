import numpy as np
import matplotlib.pyplot as plt
import time

start=time.time()
x=np.random.rand(10000)
stop=time.time()-start

print("Time taken=%f secs"%stop)
def uniform(X):
	out=[]
	for x in X:
		if x<=1 and x>=0:
			out.append(1);
		else:
			out.append(0);
	return out

plt.plot(np.linspace(0,1),uniform(np.linspace(0,1)),"k")
plt.hist(x,density=True)
plt.legend(["uniform distribution","random numbers density"])
plt.xlabel("random numbers")
plt.ylabel("density")
plt.savefig("fig1.png")
