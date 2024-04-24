#include<stdio.h>
#include<stdlib.h>
#include<math.h>


float calculate_error_bound(float t,float M, float L,double h,double a) {
    return ((h*M)/(2*L))*(exp(t-a)-1);
}

int main()
{
int x0=0;
int xf=2;
float y0=0.5;
float h=0.2;
int n=(xf-x0)/h;
float x[n];
float y[n];
float y_true[n];
float error[n];
float error_bound[n];
for(int i=0;i<=n;i++)
{
x[i]=0;
y[i]=0;
}
x[0]=x0;
x[n]=xf;
y[0]=y0;
for(int i=0;i<n;i++)
{
x[i+1]=x[i]+h;
y[i+1]=y[i]+h*(y[i]-x[i]*x[i]+1);
}
float M=1.5;
float L=1;
for(int i=0;i<=n;i++)
{
y_true[i]=(x[i]+1)*(x[i]+1)-0.5*exp(x[i]);
if(y_true[i]>=y[i])
error[i]=y_true[i]-y[i];
else 
error[i]=y[i]-y_true[i];

error_bound[i]=calculate_error_bound(x[i],M,L,h,x0);
}
printf("xi\t\tyi\t\teps_i\t\teps_bound\n");
for(int i=0;i<=n;i++)
printf("%f\t%f\t%f\t%f\n",x[i],y[i],error[i],error_bound[i]);
return 0;
}
