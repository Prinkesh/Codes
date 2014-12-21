#include <vector>
#include<iostream>
#include<stdio.h>
#define REP(i,n) for (int i = 1; i <= n; i++)
using namespace std;

typedef long long ll;
typedef vector<vector<ll> > matrix;
const ll MOD = 10000007;
const int K = 5;

// computes A * B
matrix mul(matrix A, matrix B)
{
    matrix C(K+1, vector<ll>(K+1));
    REP(i, K) REP(j, K) REP(k, K)
        C[i][j] = (C[i][j] + (A[i][k] * B[k][j]) )%MOD;
    return C;
}

// computes A ^ p
matrix pow(matrix A, ll p)
{//cout<<p<<endl;
 //getchar();
    if (p == 1)
        return A;
    if (p % 2)
        return mul(A, pow(A, p-1));
    matrix X = pow(A, p/2);
    return mul(X, X);
}

// returns the N-th term of Fibonacci sequence
int fib(ll N)
{
    // create vector F1
    vector<ll> F1(K+1);
    F1[1] = 1;
    F1[2] = 2;
    F1[3]=3;
    F1[4]=2;
    F1[5]=1;

    // create matrix T
    matrix T(K+1, vector<ll>(K+1));
    T[1][1] =0 ,T[1][2]=1 ,T[1][3]=0 ,T[1][4]=0 ,T[1][5]=0;
    T[2][1] =0 ,T[2][2]=0 ,T[2][3]=1 ,T[2][4]=0 ,T[2][5]=0;
    T[3][1] =0 ,T[3][2]=0 ,T[3][3]=0 ,T[3][4]=1 ,T[3][5]=0;
    T[4][1] =0 ,T[4][2]=0 ,T[4][3]=0 ,T[4][4]=0 ,T[4][5]=1;
    T[5][1] =1 ,T[5][2]=2 ,T[5][3]=3 ,T[5][4]=2 ,T[5][5]=1;
    //T[2][1] = 1, T[2][2] = 1;

//T={{0,0,0,0,0,0},{0,0,1,0,0,0},{0,0,0,1,0,0},{0,0,0,0,1,0},{0,0,0,0,0,1},{0,1,2,3,2,1}};
    // raise T to the (N-1)th power
    if (N == 1)
        return 1;
    T = pow(T, N-1);

    // the answer is the first row of T . F1
    ll res = 0;
    REP(i, K)
        res = (res + (T[1][i] * F1[i]) % MOD)%MOD;
    return res;
}
int main(){
    int t;
    ll i;

    scanf("%d",&t);
   // printf(" %d",t);

    while(t--){
            cin>>i;
   //         cout<<i<<endl;
        cout<<fib(i)%MOD<<endl;
      //  cout<<fib(i)<<endl;
    }

}
