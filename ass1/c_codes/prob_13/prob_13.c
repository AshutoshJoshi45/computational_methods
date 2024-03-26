#include<stdio.h>
#include<gsl/gsl_linalg.h>
int main()
{
char *fname="prob13_p1_results.txt";
FILE *fp=fopen(fname,"w");
int n=3;
double a_data[3][3]={{3,-1,1},{3,6,2},{3,3,7}};
gsl_matrix *A=gsl_matrix_alloc(n,n);
gsl_vector *b=gsl_vector_alloc(n);
int I[n][n];
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
if(i==j)
I[i][j]=1;
else
I[i][j]=0;
gsl_matrix_set(A,i,j,a_data[i][j]);
}
}
gsl_permutation *p=gsl_permutation_alloc(n);
int s;
gsl_linalg_LU_decomp(A,p,&s);
double L[n][n];
double U[n][n];
double P[n][n];
int k;
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
U[i][j]=0;
if(i==j)
L[i][j]=1;
else
L[i][j]=0;
}
}
for(int i=0;i<n;i++)
{
for(int j=i;j<n;j++)
{
U[i][j]=gsl_matrix_get(A,i,j);
}
}
for(int i=0;i<n;i++)
{
for(int j=0;j<i;j++)
{
L[i][j]=gsl_matrix_get(A,i,j);
}
}
for(int i=0;i<n;i++)
{
k=gsl_permutation_get(p,i);
for(int j=0;j<n;j++)
{
P[j][i]=I[j][k];
}
}
fprintf(fp,"The PLU factor matrices are\n");
fprintf(fp,"P=\n");
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
fprintf(fp,"%f \t",P[i][j]);
}
fprintf(fp,"\n");
}
fprintf(fp,"L=\n");
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
fprintf(fp,"%f \t",L[i][j]);
}
fprintf(fp,"\n");
}
fprintf(fp,"U=\n");
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
fprintf(fp,"%f \t",U[i][j]);
}
fprintf(fp,"\n");
}
/*Matrix Multiplication(Checking PA=LU)*/
double LU[n][n];
double PA[n][n];
double sum1,sum2;
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
sum1=0.0;
sum2=0.0;
for(int l=0;l<n;l++)
{
sum1=sum1+L[i][l]*U[l][j];
sum2=sum2+P[i][l]*a_data[l][j];
}
LU[i][j]=sum1;
PA[i][j]=sum2;
}
}
fprintf(fp,"Checking if LU decomposition is correct.\n");
fprintf(fp,"LU=\n");
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
fprintf(fp,"%f \t",LU[i][j]);
}
fprintf(fp,"\n");
}
fprintf(fp,"PA=\n");
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
fprintf(fp,"%f \t",PA[i][j]);
}
fprintf(fp,"\n");
}
gsl_vector_free(b);
gsl_permutation_free(p);
gsl_matrix_free(A);
fclose(fp);
return 0;
}
