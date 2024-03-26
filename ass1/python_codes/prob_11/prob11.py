import numpy as np
#Part 1
A=np.array([[3,-1,1],[3,6,2],[3,3,7]],dtype=np.float64)
b=np.array([1,0,4],dtype=np.float64)
x=np.linalg.solve(A,b)
print("For Part 1, x=",x)


#Part 2
A=np.array([[10,-1,0],[-1,10,-2],[0,-2,10]],dtype=np.float64)
b=np.array([9,7,6],dtype=np.float64)
x=np.linalg.solve(A,b)
print("For Part 2, x=",x)


#Part 3
A=np.array([[10,5,0,0],[5,10,-4,0],[0,-4,8,-1],[0,0,-1,5]],dtype=np.float64)
b=np.array([6,25,-11,-11],dtype=np.float64)
x=np.linalg.solve(A,b)
print("For Part 3, x=",x)


#Part 4
A=np.array([[4,1,1,0,1],[-1,-3,1,1,0],[2,1,5,-1,-1],[-1,-1,-1,4,0],[0,2,-1,1,4]],dtype=np.float64)
b=np.array([6,6,6,6,6],dtype=np.float64)
x=np.linalg.solve(A,b)
print("For Part 4, x=",x)
