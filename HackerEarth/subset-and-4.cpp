#include <stdio.h>

int main()
{int t,n,k,i,num;
scanf("%d",&t);
while(t--)
{
	scanf("%d",&n);
	scanf("%d",&k);
	for(i=0;i<k;i++)
	{scanf("%d",&num);
	n&=num;
	}
	if (n==0)
	printf("Yes\n");
	else
	printf("No\n");
}
    //printf("Hello World!\n");
    return 0;
}
