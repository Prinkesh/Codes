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
#include<mpi.h>
#include<malloc.h>
#define N 5000000
int n=10000000;
int slicesize=128*1024;
//int a[N];
//void mark(int i)
//{int j;
//printf("%d ------\n",i);
//#pragma omp parallel for private(j)
//for(j=i*i;j<=n-1;j+=2*i)
//{//printf("%d ",j);
// a[j/2]=1;

//}
//}


int blockcal(int from ,int to){
int memsize=(to-from+1)/2;
char * isPrime;
isPrime=(char *)malloc(memsize*sizeof(char));

int i;
for(i=0;i<memsize;i++){
isPrime[i]=1;
}
for(i=3;i*i<=to;i+=2)
{
/* code for discarding some higest multiples like 3,5,7,11,13 */
if ((i>=9 && i%3==0) || (i>=25 && i%5==0) || (i>=49 && i%7==0) || (i>=121 && i%11==0) || (i>=169 && i%13==0))
continue;

/* code for marking off others */

 // skip numbers before current slice
int minJ = ((from+i-1)/i)*i;
if (minJ < i*i)
	  minJ = i*i;
                    // start value must be odd
if ((minJ & 1) == 0)
          minJ += i;
  int j;                 // find all odd non-primes
for (j = minJ; j <= to; j += 2*i)
{
	int index = j - from;
        isPrime[index/2] = 0;
}

}
                                                              // count primes in this block
int found = 0;
for (i = 0; i < memsize; i++)
found+=isPrime[i];
              // 2 is not odd => include on demand
if (from <= 2)
      found++;
free(isPrime);
return found;

}




void main(int argc,char * argv[])
{int i;

int size,rank;
MPI_Init(&argc,&argv);
MPI_Comm_size(MPI_COMM_WORLD,&size);
MPI_Comm_rank(MPI_COMM_WORLD,&rank);
int chunksize=(n-1)/size;
int rem=(n-1)-(size*chunksize);

printf("\nrank - %d ,from - %d ,to - %d ,slice - %d \n",rank,(2 + rank*chunksize),(2+rank*chunksize)+chunksize,slicesize);

int cnt=0;
//int lastnumsqrt=sqrt(n-1);
int from,to;
//#pragma omp parallel for reduction(+:cnt)
for(from=(2 + rank*chunksize);from<(rank*chunksize+2)+chunksize;from+=slicesize)
{
  to=from+slicesize;
 if(to>=(rank*chunksize+2)+chunksize)
to=(rank*chunksize+2)+chunksize-1;
cnt+=blockcal(from,to); 

}
MPI_Barrier(MPI_COMM_WORLD);
int sum;
MPI_Reduce(&cnt,&sum,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);
if(rank==0){
if (rem!=0)
sum+=blockcal(((size-1)*chunksize+2)+chunksize,n-1);
printf("%d ",sum);}
/*

//#pragma omp parallel for schedule(dynamic)
for(i=3;i<=lastnumsqrt;i+=2)
	{ if (a[i/2]==0)
		mark(i);
	}   


//#pragma omp parallel for reduction(+:cnt)
for(i=1;i<=(n-1)/2;i++){
if (a[i]==0){cnt++;
}}*/
//printf("%d ",cnt);
MPI_Finalize();

}
