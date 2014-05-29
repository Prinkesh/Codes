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
#define N 10000001
int n=10000001;
int a[N];
void mark(int i)
{int j;
//printf("%d ------\n",i);
#pragma omp parallel for private(j)
for(j=i+i;j<=n-1;j+=i)
{//printf("%d ",j);
 a[j]=1;

}
}



int main()
{int i;
//for(i=0;i<=1000;i++){
//printf("%d ",a[i]);
//}
   //printf("%d")
   int cnt=0;
   for(i=2;i<=sqrt(n-1);i++)
	{ if (a[i]==0)
		mark(i);
	}   
  for(i=2;i<=n-1;i++){
if (a[i]==0){cnt++;
}}
printf("%d",cnt);


}
