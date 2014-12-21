#include <stdio.h>

int main()
{
	int x;
	
	while(1)
	{
		scanf("%d",&x);
		if (x==-1)
			break;
	if ((x&1)==0)
		printf("%d\n",x);
	}
    return 0;
}
