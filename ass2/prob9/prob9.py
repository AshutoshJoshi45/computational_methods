import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

#Part 1
def f(x,y):
	return np.array([y[1],-np.exp(-2*y[0])])
def bc(ya,yb):
	return np.array([ya[0]-0,yb[0]-np.log(2)])
x=np.linspace(1,2)
y=np.zeros((2,x.size))
#y[0,:]=np.log(x)
res=solve_bvp(f,bc,x,y)
plt.subplot(2,2,1)
plt.plot(x,res.sol(x)[0],".r")
plt.legend(["Part 1"])
plt.ylabel("y")

#Part 2
def f(x,y):
	return np.vstack((y[1],y[1]*np.cos(x)-y[0]*np.log(y[0])))
def bc(ya,yb):
	return np.array([ya[0]-1,yb[0]-np.exp(1)])
x=np.linspace(0,np.pi/2)
y=np.ones((2,x.size))
res=solve_bvp(f,bc,x,y)
plt.subplot(2,2,2)
plt.plot(res.x,res.y[0],".r")
plt.legend(["Part 2"])
#Part 3
def f(x,y):
	return np.array([y[1],-(2*y[1]**3+y[0]**2*y[1])/np.cos(x)])
def bc(ya,yb):
	return np.array([ya[0]-2**(-0.25),yb[0]-12**(0.25)/2])
x=np.linspace(np.pi/4,np.pi/3)
y=np.zeros((2,x.size))
res=solve_bvp(f,bc,x,y)
plt.subplot(2,2,3)
plt.plot(res.x,res.y[0],".r")
plt.legend(["Part 3"])
plt.xlabel("x")
plt.ylabel("y")
#Part 4
def f(x,y):
	return np.array([y[1],1/2-((y[1])**2)/2-y[0]*np.sin(x)/2])
def bc(ya,yb):
	return np.array([ya[0]-2,yb[0]-2])
x=np.linspace(0,np.pi)
y=np.zeros((2,x.size))
res=solve_bvp(f,bc,x,y)
plt.subplot(2,2,4)
plt.plot(res.x,res.y[0],".r")
plt.legend(["Part 4"])
plt.xlabel("x")
plt.show()
