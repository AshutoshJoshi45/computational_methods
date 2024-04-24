import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
#Part 1
def dydx(t,y):
	return t*np.exp(3*t)-2*y
y0=[0]
sol=solve_ivp(dydx,[0,1],y0)
def true_soln(t):
	return 1/25*np.exp(-2*t)*(1+np.exp(5*t)*(-1+5*t))
plt.subplot(2,2,1)
plt.plot(sol.t,sol.y[0],".r",np.linspace(0,1),true_soln(np.linspace(0,1)),"k")
plt.title("Part 1")
plt.ylabel("y")

#Part 2
def dydx(t,y):
	return 1-(t-y)**2
y0=[1]
sol=solve_ivp(dydx,[2,3],y0)
def true_soln(t):
	return (1-3*t+t*t)/(-3+t)
t=[]
y=[]
for i in range(np.size(sol.t)):
	if sol.y[0][i]<true_soln(2.95):
		continue
	t.append(sol.t[i])
	y.append(sol.y[0][i])
plt.subplot(2,2,2)
plt.plot(t,y,".r",np.linspace(2,3),true_soln(np.linspace(2,3)),"k")
plt.title("Part 2")


#Part 3
def dydx(t,y):
	return 1+y/t
y0=[2]
sol=solve_ivp(dydx,[1,2],y0)
def true_soln(t):
	return t*np.log(t)+2*t
plt.subplot(2,2,3)
plt.plot(sol.t,sol.y[0],".r",np.linspace(1,2),true_soln(np.linspace(1,2)),"k")
plt.title("Part 3")
plt.xlabel("t")
plt.ylabel("y")


#Part 4
def dydx(t,y):
	return np.cos(2*t)+np.sin(3*t)
y0=[1]
sol=solve_ivp(dydx,[0,1],y0)
def true_soln(t):
	return 1/6*(8-2*np.cos(3*t)+3*np.sin(2*t))
plt.subplot(2,2,4)
plt.plot(sol.t,sol.y[0],".r",np.linspace(0,1),true_soln(np.linspace(0,1)),"k")
plt.title("Part 4")
plt.xlabel("t")



plt.show()
