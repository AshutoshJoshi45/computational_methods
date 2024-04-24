#Shooting Method
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
	out=np.array([y[1],-10]) #g=10
	return out
x0=0 #Initial Time
x1=10 #Final Time
alpha=0 #Initial Position
beta=0 #Final Position
x_range=np.linspace(x0,x1)

"""
def secant_method(x0,x1,f,tol=1e-5):
	sol=[]
	while abs(x1-x0)>tol:
		temp=x1-f(x1)*(x1-x0)/(f(x1)-f(x0))
		x0=x1
		x1=temp
		print(x1)
		sol.append(x1)
	return sol
"""

def bisection_method(x0,x1,f,tol=1e-5):
	if f(x0)*f(x1)>0:
		print("Invalid Range for Bisection Method")
		return
	sol=[]
	mid=(x0+x1)/2
	while abs(x1-x0)>tol:
		mid=(x1+x0)/2
		if f(mid)*f(x0)<0:
			x1=mid
		if f(mid)*f(x1)<0:
			x0=mid
		sol.append(mid)
	return sol

def true_soln(x):
	return 50*x-5*x*x			

def shooting_method(t0,t1,dydx,x_range): #t stands for guess
	def f(t):
		temp1=rk4(np.array([alpha,t]),x_range,dydx)
		temp2=temp1[-1][0]
		return temp2-beta
	t_list=bisection_method(t0,t1,f,0.2)
	yf=[]
	for t in t_list:
		yi=np.array([alpha,t])
		y_sol=rk4(yi,x_range,dydx)
		yf.append(y_sol[-1][0]) #Optional Demonstrating np.argmin
		plt.plot(x_range,y_sol[:,0],"--",label="Guess=%f"%t)
	plt.plot(x_range,true_soln(x_range),".-r",label="True Solution")
	plt.grid()
	plt.xlabel("t(s)")
	plt.ylabel("x(m)")
	plt.legend()
	plt.title("Shooting Method")
	plt.show()
	
	yf=np.array(yf)
	
	t_best=t_list[np.argmin(abs(yf-beta))] #Using argmin to find best initial guess
	print("The best initial guess for slope=",t_best)
	
	
	return

shooting_method(30,80,dydx,x_range)
	


