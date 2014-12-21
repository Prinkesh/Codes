#include <stdio.h>
#define ma 300000000
int main()
{
	long long x,n,cnt=0;
	scanf("%lld",&n);
	while(n--)
	{
		scanf("%lld",&x);
		if (x<ma)
			cnt++;
	}
	printf("%lld",cnt);
    return 0;
}
