#include <iostream>
using namespace std;
 
 
    int reversDigits(int num)
    {
        int rev_num = 0;
        while(num > 0)
        {
            rev_num = rev_num*10 + num%10;
            num = num/10;
        }
        return rev_num;
    }
 
int main()
{
   int  i=3;
      int a[2000001];
 
 
    for (int ii=1;ii<=2000000;ii++)
    {  if(ii%2==0)
       a[ii]=0;
        else
    	a[ii]=1;
    }
 
   while (i<=2000000)
   {
 
   if(a[i]==1)
   {
 
   	int k=2;
   for(int j=i*k;j<2000000;k++,j=i*k)
   {
   	if(j<2000000)
   	a[j]=0;
 
   }
 
   }
      i=i+2;
    }
 
  for (int z=13;z<=1000000;z++)
 
   {
	   int number =z;
	   int revnum=reversDigits(z);
	   if (a[number]==1 && number!=revnum && a[revnum]==1)
	   {
	   	a[revnum]=0;
	   	 cout<<z<<"\n";
	   }
 
 
   }
 
 
 
   }
Language: C++
