import numpy as np
import matplotlib.pyplot as plt
def rk4(y_initial,x_range,dydx): #y_initial should be an array
	n=np.size(x_range)
	y=np.zeros((n,3))
	h=x_range[1]-x_range[0]
	y[0]=y_initial
	for i in range(np.size(x_range)-1):
		k1=h*dydx(x_range[i],y[i])
		k2=h*dydx(x_range[i]+h/2,y[i]+k1/2)
		k3=h*dydx(x_range[i]+h/2,y[i]+k2/2)
		k4=h*dydx(x_range[i+1],y[i]+k3)
		y[i+1]=y[i]+1/6*(k1+2*k2+2*k3+k4)
	return y
def dydx(x,y):
	out=np.array([y[0]+2*y[1]-2*y[2]+np.exp(-x),y[1]+y[2]-2*np.exp(-x),y[0]+2*y[1]+np.exp(-x)])
	return out

u=rk4(np.array([3,-1,1]),np.linspace(0,1),dydx)
plt.plot(np.linspace(0,1),u[:,0],".-r")	
plt.plot(np.linspace(0,1),u[:,1],".-c")
plt.plot(np.linspace(0,1),u[:,2],".-g")
plt.grid()
plt.legend(["u1","u2","u3"])
plt.xlabel("t")
plt.ylabel("u")
plt.show()
