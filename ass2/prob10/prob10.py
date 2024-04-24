import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
	return (y**2+y)/x


def RKF(f,a,b,alpha,tol,hmax,hmin):
	T=[]
	W=[]
	T.append(a)
	W.append(alpha)
	t=a
	w=alpha
	h=hmax
	flag=1
	while flag==1:
		if h==0:
			print("fail")
			break
		k1=h*f(t,w)
		k2=h*f(t+h/3,w+k1/4)
		k3=h*f(t+3*h/8,w+3/32*k1+9/32*k2)
		k4=h*f(t+12/13*h,w+1932/2197*k1-7200/2197*k2+7296/2197*k3)
		k5=h*f(t+h,w+439/216*k1-8*k2+3680/513*k3-845/4104*k4)
		k6=h*f(t+h/2,w-8/27*k1+2*k2-3544/2565*k3+1859/4104*k4-11/40*k5)
		R=abs(1/360*k1-128/4275*k3-2197/75240*k4+1/50*k5+2/55*k6)/h
		if R<=tol:
			t=t+h
			w=w+25/216*k1+1408/2565*k3+2197/4104*k4-1/5*k5
			T.append(t)
			W.append(w)
		q=0.84*(tol/R)**(1/4)
		h=q*h
		if h>hmax:
			h=hmax
		if t>=b:
			flag=0
		elif t+h>b:
			h=b-t
		elif h<hmin:
			flag=0
			print("Minimum h exceeded, process completed unsuccessfully")
	return T,W
x,y=RKF(f,1,3,-2,1e-4,1,0.01)

def true_soln(x):
	return 2*x/(1-2*x)
#print(x)
plt.plot(x,y,"^r")
plt.plot(np.linspace(1,3),true_soln(np.linspace(1,3)),"-k")	
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["RKF Method","True Solution"])
plt.title("Runge-Kutta-Fehlberg Method")
plt.grid()
plt.show()	
