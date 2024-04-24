import numpy as np
import matplotlib.pyplot as plt
def f(x,y,dydx): #f(x,y,y')
	out=-10
	return out
alpha=0 #initial y
beta=0 #final y
a=0 #initial x
b=10 #final x
h=0.1
x_range=np.arange(a,b+h,h)
w=np.zeros_like(x_range)
w[0]=alpha
w[-1]=beta

n=np.size(w)-2

A=np.zeros((n,n))
A[0,0]=-2/h**2
A[1,0]=1/h**2
A[0,1]=1/h**2
A[n-1,n-1]=-2/h**2
A[n-1,n-2]=1/h**2
A[n-2,n-1]=1/h**2
for i in range(1,n-1):
	for j in range(1,n-1):
		if i==j:
			A[i,j]=-2/h**2
		if i==j+1 or i==j-1:
			A[i,j]=1/h**2

def rhs_cal(f,w_guess,x_range): 
#w_guess is a list/array of w's apart from alpha and beta i.e. w=[alpha,w_guess,beta]
	b=np.zeros(n)
	b[0]=f(x_range[1],w_guess[0],(w_guess[1]-alpha)/(2*h))-alpha
	b[-1]=f(x_range[-2],w_guess[-1],(beta-w_guess[-2])/(2*h))-beta
	for i in range(1,n-1):
		b[i]=f(x_range[i+1],w_guess[i],(w_guess[i+1]-w_guess[i])/(2*h))
	rhs=np.linalg.inv(A)@b
	return rhs
	
maxiter=100
tol=0.01

def true_soln(x):
	return 50*x-5*x*x
wi=true_soln(x_range[1:-1])+1

for i in range(maxiter):
	temp=rhs_cal(f,wi,x_range)
	diff=abs(max(temp-wi))
	yi=[alpha]+wi.tolist()+[beta]
	#plt.plot(x_range,yi)
	wi=temp
	if diff<tol:
		break
#print(wi)
plt.plot(x_range,yi,".r",label="FDM")
plt.plot(np.linspace(a,b),true_soln(np.linspace(a,b)),"-k",label="True Solution")
plt.xlabel("t(s)")
plt.ylabel("x(m)")
plt.title("Finite Difference Method")
plt.legend()
plt.grid()
print(i)	
plt.show()
	
	
	
	
	
	
	
	
	
	
