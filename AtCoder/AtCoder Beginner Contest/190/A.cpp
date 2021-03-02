#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int A,B,C;
    cin >> A >> B >> C;

  		if(C==0&&A>B){
        	cout << "Takahashi" << endl;
        }
  		else if(C==0&&A<=B){
        	cout << "Aoki" << endl;
        }
  		else if(C==1&&A>=B){
        	cout << "Takahashi" << endl;
        }
  		else if(C==1&&A<B){
        	cout << "Aoki" << endl;
        }

    return 0;
}
