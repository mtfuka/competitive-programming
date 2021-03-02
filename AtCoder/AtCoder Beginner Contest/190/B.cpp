#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N,S,D;
    cin >> N >> S >> D;
  	vector<vector<int>> A(N,vector<int>(2));
    rep(i, N) {
        rep(j, 2){
        	cin >> A[i][j];
        }
    }
  	bool a=false;
  	rep(i, N) {
        if(A[i][0]<S&&A[i][1]>D) a=true;
    }

 	if(a) cout << "Yes" << endl;
  	else cout << "No" << endl;
    return 0;
}
