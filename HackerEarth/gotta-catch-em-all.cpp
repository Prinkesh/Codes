#include <iostream>
#include <algorithm> 
using namespace std;

int main()
{
    int k, p[1000001],max =0;
    cin >> k;
    for(int i=0;i<k;i++)
      cin >> p[i] ;  
     
     sort(p, p+k);
     
    for(int i=k-1,j=1;i>-1;i--,j++) if(p[i]+j > max) max =  p[i]+j ;
     
    cout << max+1;
    
    return 0;
}
