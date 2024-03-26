import numpy as np
print("\nI have used the L-Inf Norm to compare to the true vector\n")
def conjugate_gradient(A,b,x_true,x_guess):
	r=b-A@x_guess
	temp1=max(x_guess)
	temp2=max(x_true)
	count=0
	while abs(temp2-temp1)>0.01:
		v=r
		t=(v@v)/(v@(A@v))
		x_guess=x_guess+t*v
		temp1=max(x_guess)
		r=b-A@x_guess
		count=count+1
	print("Count=",count)
	return x_guess
def relaxation_method(A,b,x_true,x_guess):
    n=np.size(b)
    omega=1.25
    count=0
    temp1=max(x_guess)
    temp2=max(x_true)
    while abs(temp2-temp1)>0.01:
        for i in range(n):
            r=b-A@x_guess
            x_guess[i]=x_guess[i]+omega*r[i]/A[i,i]
        count=count+1
        temp1=max(x_guess)
    print("Count=",count)
    return x_guess
def jacobi_method(A,b,x_true,x_guess):
    n=np.size(b)
    x0=x_guess
    x1=[]
    temp1=max(x_guess)
    temp2=max(x_true)
    count=0
    while abs(temp2-temp1)>0.01:
        for i in range(n):
            s=0
            for j in range(n):
                if i!=j:
                    s=s-A[i,j]*x0[j]
            x1.append((s+b[i])/A[i,i])
        temp1=max(x1)
        x0=x1
        x1=[]
        count=count+1
    print("Count=",count)
    return x0
    
def gauss_seidel(A,b,x_true,x_guess):
    n=np.size(b)
    x0=x_guess
    temp0=max(x0)
    temp1=max(x_true)
    count=0
    x_prev=np.zeros_like(x0)
    while (abs(temp0-temp1)>0.01):
        for i in range(n):
            s=0
            for j in range(n):
                if j!=i:
                    s=s-A[i,j]*x0[j]    
            x0[i]=1/A[i,i]*(s+b[i])
        temp0=max(x0)
        count=count+1
    print("Count=",count)
    return x0
#main block
A=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]],dtype=np.float64)
b=np.array([1,2,3,4,5],dtype=np.float64)
x_true=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163],dtype=np.float64)
x_guess=np.array([0,0,0,0,0],dtype=np.float64)
print("\nConjugate Gradient Method")
print(conjugate_gradient(A,b,x_true,x_guess))
x_guess=np.array([0,0,0,0,0],dtype=np.float64)
print("\nRelaxation Method")
print(relaxation_method(A,b,x_true,x_guess))
x_guess=np.array([0,0,0,0,0],dtype=np.float64)
print("\nJacobi Method")
print(jacobi_method(A,b,x_true,x_guess))
x_guess=np.array([0,0,0,0,0],dtype=np.float64)
print("\nGauss Seidel Method")
print(gauss_seidel(A,b,x_true,x_guess))






