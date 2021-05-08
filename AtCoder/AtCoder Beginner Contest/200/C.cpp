#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N;
    cin >> N;
    vector<int> A(N);
    rep(i, N) {
        cin >> A[i];
    }
    long long d[200] = {0};
    rep(i,N){
    	d[A[i]%200] += 1;
    }
    long long ans = 0;
    rep(i,200){
    	ans += d[i]*(d[i]-1)/2;
    }
    cout << ans << endl;
}