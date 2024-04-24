import numpy as np
import matplotlib.pyplot as plt
def dydx(y,t):
	return y/t-(y/t)**2
def soln(t):
	return t/(1+np.log(t))
	
def euler(t_range,y_initial,dydx):
	y=np.zeros_like(t_range)
	y[0]=y_initial
	h=t_range[1]-t_range[0]
	for i in range(np.size(t_range)-1):
		y[i+1]=y[i]+h*dydx(y[i],t_range[i])
	return y
h=0.1
t_range=np.arange(1,2+h,h)
yi=1
y_euler=euler(t_range,yi,dydx)
y_soln=soln(t_range[:])
err=abs(y_euler[:]-y_soln[:])
rel_err=err[:]/y_soln[:]
for i in zip(t_range,y_euler,y_soln,err,rel_err):
	print(i)
err_total=sum(err)
rel_err_total=sum(rel_err)
print("Total Error=",err_total)
print("Total Relative Error=",rel_err_total)

#In order to save memory, I have copied the result from the terminal window and pasted in a text file.

plt.plot(t_range,y_euler,".k",t_range,y_soln,".-k")
plt.xlabel("t")
plt.ylabel("y")
plt.legend(["Euler Method","True Solution"])
plt.grid()
plt.show()
