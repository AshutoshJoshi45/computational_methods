import numpy as np
A=np.array([[5,-2],[-2,8]])
diff=np.inf
tol=1e-10
maxiter=10
i=0
while (i<maxiter):
	Q,R=np.linalg.qr(A)
	A=R@Q
	i=i+1
print("Using QR Decomposition")
print("No. of iterations",i)
print("Diag(A)=\n",A)
print("Eigenvals=",np.diag(A))
eigvals,eigvecs=np.linalg.eigh(A)
print("\nUsing np.linalg.eigh\nEigenvals=",eigvals)
