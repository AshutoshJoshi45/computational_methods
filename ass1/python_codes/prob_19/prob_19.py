import numpy as np
import time
def svd_check(A):
	m,n=np.shape(A)
	temp=np.transpose(A)@A
	eigvals=np.linalg.eigh(temp)[0]
	print("A=\n",A)
	print("Eigenvalues of A'A=",np.sort(eigvals))
	print("Square root of eigenvals=",np.sqrt(np.sort(eigvals)))
	start=time.process_time()
	U,S,V=np.linalg.svd(A)
	stop=time.process_time()
	print("Time taken to compute SVD using numpy=",stop-start,"secs")
	print("S=",S)
	S_mat=np.zeros_like(A,dtype=np.float64)
	for i in range(m):
		for j in range(n):
			if i==j:
				S_mat[i,j]=S[i]
	print("S matrix=\n",S_mat)
	print("U matrix=\n",U)
	print("V' matrix=\n",V)
	print("USV'=\n",U@S_mat@V)
	print("\n")
	return
A=np.array([[2,1],[1,0]])
svd_check(A)
A=np.array([[2,1],[1,0],[0,1]])
svd_check(A)
A=np.array([[2,1],[-1,1],[1,1],[2,-1]])
svd_check(A)
A=np.array([[1,1,0],[-1,0,1],[0,1,-1],[1,1,-1]])
svd_check(A)
A=np.array([[1,1,0],[-1,0,1],[0,1,-1],[1,1,-1]])
svd_check(A)
A=np.array([[0,1,1],[0,1,0],[1,1,0],[0,1,0],[1,0,1]])
svd_check(A)
