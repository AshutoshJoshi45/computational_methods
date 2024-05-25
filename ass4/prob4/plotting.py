import numpy as np
import matplotlib.pyplot as plt

def exponential_pdf(x, lam):
    return lam * np.exp(-lam * x)

mean = 0.5
lam = 1 / mean

x_values = np.linspace(0, 6, 1000)
y_values = exponential_pdf(x_values, lam)

x=np.loadtxt("expoential_deviates.txt")
plt.hist(x,bins=20,density=True)
plt.plot(x_values,y_values,"k")

plt.legend(["exponential distribution(mean=0.5)","random numbers histogram"])
plt.xlabel("random numbers")
plt.ylabel("density")
plt.savefig("fig1.png")
