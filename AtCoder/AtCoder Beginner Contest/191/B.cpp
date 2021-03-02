#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N,X;
    cin >> N >> X;
    vector<int> A(N);
    rep(i, N) {
        cin >> A[i];
    }
  	rep(i,N){
    	if(A[i]==X){
        	cout << "";
        }
      	else
        	cout << A[i] <<" ";
    }
    return 0;
}
