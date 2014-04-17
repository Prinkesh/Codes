#include <vector>
#include<iostream>
#include<stdio.h>
#define LOOP(i,n) for (int i = 1; i <= n; i++)
using namespace std;

typedef long long ll;
typedef vector<vector<ll> > matrix;
const ll MOD = 10000007;
const int K = 5;
//here k = 5 , (k+1 X k+1) matrix is taken just for simplicity
// computes A * B
matrix mul(matrix A, matrix B)
{
    matrix C(K+1, vector<ll>(K+1));
    LOOP(i, K) LOOP(j, K) LOOP(k, K)
        C[i][j] = (C[i][j] + (A[i][k] * B[k][j]) )%MOD;
    return C;
}

// computes A ^ p
matrix pow(matrix A, ll p)
{
    if (p == 1)
        return A;
    if (p % 2)
        return mul(A, pow(A, p-1));
    matrix X = pow(A, p/2);
    return mul(X, X);
}

// returns the N-th term of linear recurrence
int linear_recc(ll N)
{
    // create vector F1
    vector<ll> F1(K+1);
    F1[1] = 1;
    F1[2] = 2;
    F1[3]=3;
    F1[4]=2;
    F1[5]=1;

    // create matrix T
    matrix M(K+1, vector<ll>(K+1));
    M[1][1] =0 ,M[1][2]=1 ,M[1][3]=0 ,M[1][4]=0 ,M[1][5]=0;
    M[2][1] =0 ,M[2][2]=0 ,M[2][3]=1 ,M[2][4]=0 ,M[2][5]=0;
    M[3][1] =0 ,M[3][2]=0 ,M[3][3]=0 ,M[3][4]=1 ,M[3][5]=0;
    M[4][1] =0 ,M[4][2]=0 ,M[4][3]=0 ,M[4][4]=0 ,M[4][5]=1;
    M[5][1] =1 ,M[5][2]=2 ,M[5][3]=3 ,M[5][4]=2 ,M[5][5]=1;



    // raise M to the (N-1)th power
    if (N == 1)
        return 1;
    M = pow(M, N-1);

    // the answer is the first row of M . F1
    ll result = 0;
    LOOP(i, K)
        result = (result + (M[1][i] * F1[i]) % MOD)%MOD;
    return result;
}
int main(){
    int t;
    ll i;

    scanf("%d",&t);


    while(t--){
            cin>>i;
            cout<<linear_recc(i)<<endl;

    }

}
