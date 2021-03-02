#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    double V,T,S,D;
    cin >> V >> T >> S >> D;

  		if(D/V<T || S<D/V){
        	cout << "Yes" << endl;
        }
  		else{
        	cout << "No" << endl;
        }

    return 0;
}
