#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
	int N;//数字ではなく文字列として最初から入力すれば良い
	cin >> N;
  	vector<int> A(N);
    rep(i, N) {
        cin >> A[i];
    }

  	int ans=0;
 	while (true){//whileの条件はとりあえずtrueとして進める。 全て偶数という条件にするのは難しい
  		bool a=true;//全て偶数かどうか判定するフラグ
    	rep(i,N){
            if(A[i]%2==1){
            	a=false;//奇数があったらフラグをfalseにする
              	break;//奇数があったらその時点でroopを抜ける
            }
          	else A[i]/=2;
   		}
    	if(a) ans++;//偶数の時はカウント
      	else break;//奇数があったらwhileのループを抜ける
    }
	cout << ans << endl;
    return 0;
}
