#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int A,B,C,D;
    cin >> A >> B >> C >> D;
  	if((A+B)>(C+D)) cout << "Left" << endl;
  	if((A+B)==(C+D)) cout << "Balanced" << endl;
  	if((A+B)<(C+D)) cout << "Right" << endl;
    return 0;
}
