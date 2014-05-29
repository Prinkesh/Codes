/*
 * =====================================================================================
 *
 *       Filename:  prime_op.c
 *
 *    Description:  
 *
 *        Version:  1.0
 *        Created:  Wednesday 28 May 2014 04:49:52  IST
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (), 
 *   Organization:  
 *
 * =====================================================================================
 */
#include<stdio.h>
#include<math.h>
#include<omp.h>
#define N 5000000
int n=10000001;
int a[N];
void mark(int i)
{int j;
//printf("%d ------\n",i);
#pragma omp parallel for private(j)
for(j=i*i;j<=n-1;j+=2*i)
{//printf("%d ",j);
 a[j/2]=1;

}
}



int main()
{int i;
//for(i=0;i<=1000;i++){
//printf("%d ",a[i]);
//}
   //printf("%d")
int cnt=1;
int lastnumsqrt=sqrt(n-1);
#pragma omp parallel for schedule(dynamic)
for(i=3;i<=lastnumsqrt;i+=2)
	{ if (a[i/2]==0)
		mark(i);
	}   


#pragma omp parallel for reduction(+:cnt)
for(i=1;i<=(n-1)/2;i++){
if (a[i]==0){cnt++;
}}
printf("%d",cnt);


}
