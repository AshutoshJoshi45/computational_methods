import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

data=np.loadtxt("data",skiprows=5,usecols=(1,2,3))
x_data=data[:,0]
y_data=data[:,1]
y_err=data[:,2]

def model(theta,x):
	a,b,c=theta
	return a*x**2+b*x+c

def log_prior(theta):
	a,b,c=theta
	if -1e3<a<1e3 and -1e3<b<1e3 and -1e3<c<1e3:
		return 0
	return -np.inf	
	
def log_likelihood(theta,x,y,y_err):
	model_y=model(theta,x)
	return -0.5*np.sum(((y-model_y)/y_err)**2)

def log_posterior(theta,x,y,y_err):
	lp=log_prior(theta)
	if not np.isfinite(lp):
		return -np.inf
	return lp+log_likelihood(theta,x,y,y_err)

ndim=3
nwalkers=50
in_pos=np.random.randn(nwalkers,ndim)
sampler=emcee.EnsembleSampler(nwalkers,ndim,log_posterior,args=(x_data,y_data,y_err))

nsteps=4000
sampler.run_mcmc(in_pos,nsteps,progress=True)
samples=sampler.get_chain(discard=1000,flat=True)

fig,axs=plt.subplots(ndim,figsize=(10,7))
for i in range(ndim):
	ax=axs[i]
	ax.plot(sampler.get_chain()[:,:,i],"k")
	ax.set_ylabel(["a","b","c"][i])
axs[-1].set_xlabel("Step")
plt.savefig("fig1")
plt.close()

fig = corner.corner(samples, labels=["a", "b", "c"], truths=[0, 0, 0])
plt.savefig("fig2")
plt.close()

medians=np.median(samples,axis=0)
sigma=np.std(samples,axis=0)
 
print(f"Median values: a = {medians[0]}, b = {medians[1]}, c = {medians[2]}")
print(f"One-sigma uncertainties: a = {sigma[0]}, b = {sigma[1]}, c = {sigma[2]}")

xvals=np.linspace(min(x_data),max(x_data))
best_fit = model(medians, xvals)

for a, b, c in samples[np.random.randint(len(samples), size=200)]:
    plt.plot(xvals, model([a, b, c], xvals), color='gray', alpha=0.01)

plt.errorbar(x_data, y_data,y_err,fmt=".k", label='Data')
plt.plot(xvals, best_fit,"k",label='Best-fit model')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.savefig("fig3")

