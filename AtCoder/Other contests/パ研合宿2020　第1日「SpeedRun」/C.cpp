#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N;
    cin >> N;
    map<string,int> mp;
    rep(i,N){
        int k;
        cin >> k;
        rep(j,k){
            string S;
            cin >> S;
            mp[S]++;
        }
    }
    int ans = 0;
    for(auto p : mp){
        if(p.second==N) ans++;
    }
    cout << ans << endl;
    return 0;
}