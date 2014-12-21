#include <stdio.h>

int main()
{
	long long x;
	
	while(1)
	{
		scanf("%lld",&x);
		if (x==-1)
			break;
	if ((x&1)==0)
		printf("%lld\n",x);
	}
    return 0;
}
