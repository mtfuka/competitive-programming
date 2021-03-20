#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    string S;
    cin >> S;

    reverse(S.begin(), S.end());
	while(S.size()>0){
    	if(S.substr(0,5)=="maerd") S.erase(0,5);
      	else if(S.substr(0,7)=="remaerd") S.erase(0,7);
      	else if(S.substr(0,5)=="esare") S.erase(0,5);
      	else if(S.substr(0,6)=="resare") S.erase(0,6);
      	else{
          cout << "NO" << endl;
          return 0;
        }
    }
    cout << "YES" << endl;
    return 0;
}
