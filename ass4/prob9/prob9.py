import numpy as np
import matplotlib.pyplot as plt

def f(x): #target distribution
	if x>=3 and x<=7:
		return 1;
	else:
		return 0;

nrand=10000
x=[5]
rejected=[]
accepted=[]
c_acc=[]
c_rej=[]
for i in range(nrand):
	temp=np.random.normal(x[-1]) #I used pythons inbuilt function as proposal in the interest of time, else we can use box muller method as well
	alpha=f(temp)/f(x[-1])
	u=np.random.uniform(0,1)
	if u<=alpha:
		x.append(temp)
		accepted.append(temp)
		c_acc.append(i)
	else:
		x.append(x[-1])
		rejected.append(temp)
		c_rej.append(i)
plt.plot(c_acc,accepted,".-b",c_rej,rejected,".r")
plt.legend(["accepeted","rejected"])
plt.text(0,9,"n_samples=%d"%nrand,fontsize=12)
plt.xlabel("counts")
plt.ylabel("proposed sample")
#plt.savefig("fig1")
plt.close()

plt.hist(x,bins=15,density=True)
plt.xlabel("sample")
plt.ylabel("density")
plt.savefig("fig2")

