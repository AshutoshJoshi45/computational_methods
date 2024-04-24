import numpy as np
import matplotlib.pyplot as plt

def secant_method(x0,x1,f,tol=1e-5):
	while abs(x1-x0)>tol:
		temp=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
		x0=x1
		x1=temp
	return x1

def bwd_euler(x_range,y_initial,dydx):
	y=np.zeros_like(x_range)
	y[0]=y_initial
	h=x_range[1]-x_range[0]
	for i in range(np.size(x_range)-1):
		def f(t):
			return t-y[i]-h*dydx(x[i+1],t)
		y[i+1]=secant_method(y[i],y[i]+1,f)
	return y

#Part 1
def dydx1(x,y):
	dydx=-9*y
	return dydx
x=np.linspace(0,1)
yi=np.exp(1)
y=bwd_euler(x,yi,dydx1)
plt.plot(x,y,"^-k")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.title(r"$\frac{dy}{dx}=-9y$")
plt.show()
	
#Part 2
def dydx2(x,y):
	dydx=-20*(y-x)**2+2*x
	return dydx
x=np.linspace(0,1)
yi=1/3
y=bwd_euler(x,yi,dydx2)
plt.plot(x,y,"^-k")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.title(r"$\frac{dy}{dx}=-20(y-x)^2+2x$")
plt.show()

