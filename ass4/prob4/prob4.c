#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double cdf_inverse(double x,double lam)
{
double y=-1/lam*log(1-x);
return y;
}


int main()
{
int n=10000;
double u[n];
for (int i=0;i<n;i++)
{
u[i]=(double)rand()/(RAND_MAX);
}


double mean=0.5;
double lam=1/mean;
double x[n];
for(int i=0;i<n;i++)
{
x[i]=cdf_inverse(u[i],lam);
}
for(int i=0;i<n;i++)
{
printf("%f\n",x[i]);
}
return 0;
}
