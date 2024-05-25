import numpy as np

def vol_hypersphere(dim):
	nrand=100000
	x=[]
	for i in range(dim):
		x.append(np.random.uniform(-1,1,size=nrand))
	count=0
	for i in range(nrand):
		sum1=0
		for j in range(dim):
			sum1=sum1+x[j][i]**2
		if sum1<1:
			count=count+1
	vol_box=2**dim
	vol_hs=count*vol_box/nrand
	return vol_hs

print("Area of a unit circle=",vol_hypersphere(2))
print("Volume of a 10d sphere=",vol_hypersphere(10))
