#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N;
    cin >> N;
  	int ans=1000000001;
  	for(int i = 0; i < N; i++){
        int A,P,X;
        cin >> A >> P >> X;
        if(X-A > 0 && ans > P) ans=P;
    }


 	if(ans==1000000001) cout << -1 << endl;
  	else cout << ans << endl;
    return 0;
}
