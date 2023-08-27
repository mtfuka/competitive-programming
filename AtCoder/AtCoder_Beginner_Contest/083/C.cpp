#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int64_t X,Y;//10^-8~10^8の時はint64_t
    cin >> X >> Y;
  	int ans=0;
	while(X<=Y){
    	X*=2;
      	ans++;
    }
  	cout << ans << endl;
    return 0;
}
