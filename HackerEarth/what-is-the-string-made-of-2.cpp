#include <stdio.h>

int main()
{   //char n[101];
    char n[101];
    int a[10]={6,2,5,5,4,5,6,3,7,6};
    scanf("%s",n);
    //int rem;
    int cnt=0;
    //int num = n/10;
   // n=n/10;
   int i=0;
    while(n[i]!='\0')
    {
    	
    //	printf("%c\n",n[i]);
    	cnt+=a[((int)n[i])-48];
    	i++;
    }
    
    
    printf("%d",cnt);
    return 0;
}
