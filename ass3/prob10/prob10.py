import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath

def f(x,y):
	return np.exp(-(x**2 + y**2))
def ft(k1,k2):
	return 0.5*np.exp(-(k1**2+k2**2)/4)
N=128
x_min=-10
y_min=-10
x_max=10
y_max=10

x=np.linspace(x_min,x_max,N)
y=np.linspace(y_min,y_max,N)
delx=x[1]-x[0]
dely=y[1]-y[0]
X,Y=np.meshgrid(x,y)
Z=f(X,Y)

"""
fig=plt.figure()
ax=plt.axes(projection="3d")
ax.plot_surface(X,Y,Z)
plt.show()
"""

z=np.zeros((N,N))
for i in range(N):
	for j in range(N):
		z[i][j]=f(x[i],y[j])

z_dft=np.fft.fft2((z),norm="ortho")
kx=2*np.pi*np.fft.fftfreq(N,delx)
ky=2*np.pi*np.fft.fftfreq(N,dely)
#z_dft=np.fft.fftshift(z_dft)

zt_vals=np.zeros_like(z)
for i in range(N):
	for j in range(N):
		zt_vals[i][j]=np.abs(delx*dely*N/(2*np.pi)*cmath.exp(-1j*((x_min*kx[i])+(y_min*ky[j]))) * z_dft[i][j])
		
Kx,Ky=np.meshgrid(kx,ky)
zt_analytic=ft(Kx,Ky)

fig,ax=plt.subplots(1,2,figsize=(10,5),subplot_kw={"projection":"3d"})
ax[0].scatter(Kx.flatten(),Ky.flatten(),np.transpose(zt_vals).flatten(),c=np.abs(np.transpose(zt_vals)).flatten(),cmap="viridis")
ax[1].scatter(Kx.flatten(),Ky.flatten(),zt_analytic.flatten(),c=np.abs(zt_analytic).flatten(),cmap="viridis")

ax[0].set_xlabel("kx")
ax[0].set_ylabel("ky")
ax[0].set_zlabel(r"$\tilde{f}(k_x,k_y)$")
ax[0].set_title("np.fft.fft")

ax[1].set_xlabel("kx")
ax[1].set_ylabel("ky")
ax[1].set_zlabel(r"$\tilde{f}(k_x,k_y)$")
ax[1].set_title("analytic result")

plt.savefig("fig")

