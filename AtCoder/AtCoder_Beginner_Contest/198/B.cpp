#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N;
    cin >> N;
    if(N==0){
        cout << "Yes" << endl;
        return 0;
    }
    while(true){
        if(N%10==0) N/=10;
        else break;
    }
    string n = to_string(N);
    rep(i,n.size()/2+1){
        if(n.at(i)!=n.at(n.size()-1-i)){
            cout << "No" << endl;
            return 0;
        }
    }
    cout << "Yes" << endl;
    return 0;
}