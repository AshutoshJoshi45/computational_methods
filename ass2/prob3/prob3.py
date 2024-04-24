import numpy as np
import matplotlib.pyplot as plt
def rk4(y_initial,x_range,dydx): #y_initial should be an array
	n=np.size(x_range)
	y=np.zeros((n,2))
	h=x_range[1]-x_range[0]
	y[0]=y_initial
	for i in range(np.size(x_range)-1):
		k1=h*dydx(x_range[i],y[i])
		k2=h*dydx(x_range[i]+h/2,y[i]+k1/2)
		k3=h*dydx(x_range[i]+h/2,y[i]+k2/2)
		k4=h*dydx(x_range[i+1],y[i]+k3)
		y[i+1]=y[i]+1/6*(k1+2*k2+2*k3+k4)
	return y
def dydx(x,y): #y=[y,y']
	out=np.array([y[1],2*y[1]-y[0]+x*np.exp(x)-x])
	return out

x=np.linspace(0,1)
yi=np.array([0,0])
y_soln=rk4(yi,x,dydx)
plt.plot(x,y_soln[:,0],".-k")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.savefig("figure_1")
plt.show()
