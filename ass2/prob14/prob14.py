import numpy as np
import matplotlib.pyplot as plt
def euler(y_initial,x_range,dydx): #y_initial should be an array
	n=np.size(x_range)
	y=np.zeros((n,2))
	h=x_range[1]-x_range[0]
	y[0]=y_initial
	for i in range(np.size(x_range)-1):
		y[i+1]=y[i]+h*dydx(x_range[i],y[i])
	return y
def dydx(x,y):
	out=np.array([y[1],(2*x*y[1]-2*y[0]+x**3*np.log(x))/x**2])
	return out
h=0.001
t=np.arange(1,2+h,h)
y_initial=np.array([1,0])
y=euler(y_initial,t,dydx)
def true_soln(x):
	return 7*x/4+t**3/2*np.log(t)-3/4*t**3

plt.plot(t,y[:,0],".r",t,true_soln(t),"k")
plt.legend(["Euler Method","True Solution"])
plt.xlabel("t")
plt.ylabel("y")
plt.grid()
plt.show()
