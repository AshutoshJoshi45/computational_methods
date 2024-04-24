"""
We set u=-1/(1+t)
=> du/dt=1/(1+t)^2
=>the diff eqn can be written as dx/du=1/(u^2 x^2+(1+u)^2)
where -1<=u<=0 
"""
import numpy as np
import matplotlib.pyplot as plt
def dxdu(u,x):
	return 1/(u**2 * x**2 + (1+u)**2)

def u(t):
	return -1/(1+t)

def t(u):
	return -1-1/u

def rk4(y_initial,x_range,dydx):
	n=np.size(x_range)
	y=np.zeros(n)
	h=x_range[1]-x_range[0]
	y[0]=y_initial
	for i in range(np.size(x_range)-1):
		k1=h*dydx(x_range[i],y[i])
		k2=h*dydx(x_range[i]+h/2,y[i]+k1/2)
		k3=h*dydx(x_range[i]+h/2,y[i]+k2/2)
		k4=h*dydx(x_range[i+1],y[i]+k3)
		y[i+1]=y[i]+1/6*(k1+2*k2+2*k3+k4)
	return y

a=u(0)
b=u(3.5*10**6)
u_range=np.linspace(a,b)
alpha=1
x=rk4(alpha,u_range,dxdu)
plt.plot(u_range,x,".-k")
plt.xlabel(r"$\frac{-1}{1+t}$")
plt.ylabel("x")
plt.show()
print("The value of x at t=%f is %f"%(t(u_range[-1]),x[-1]))
