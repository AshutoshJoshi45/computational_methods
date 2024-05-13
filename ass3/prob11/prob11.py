import numpy as np
import matplotlib.pyplot as plt

def box(x):
	if x<-1 or x>1:
		return 0;
	else:
		return 1;

x_range=np.linspace(-10,10,256)

convolution=np.convolve([box(x) for x in x_range], [box(x) for x in x_range],"same")*(x_range[1]-x_range[0])

plt.plot(x_range,[box(x) for x in x_range],".-r",x_range,convolution,".-c")
plt.legend(["box function","convolution"])
plt.savefig("fig")
