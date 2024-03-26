import numpy as np
A=[[2,-1,0],[-1,2,-1],[0,-1,2]]
n,m=np.shape(A)
x_guess=np.array([1,1,1])
vec=np.array([1,2,3])
diff=np.inf
tol=0.01
lam1=0
while diff>tol:
	lam0=lam1
	x_guess=A@x_guess
	lam1=(A@x_guess)@vec/(x_guess@vec)
	diff=abs(lam1-lam0)/abs(lam1)
print("Dominant Eigenvalue Using Power Method=\n",lam1)
eigvals=np.linalg.eigh(A)[0]
print("Dominant Eigenvalue Using np.linalg.eigh=\n",max(eigvals))
print("Percentage error=",(abs(lam1-max(eigvals))/lam1*100))
