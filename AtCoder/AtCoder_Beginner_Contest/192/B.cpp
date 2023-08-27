#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
  	string X;
  	cin >> X;
  	//int N
  	//N = X.size();
  	int N=X.length();//宣言と代入一緒にできる
  	//vector<char> A(N);配列にしなくてもstringの1文字にはs[i]でアクセスできる
    //rep(i, N) {
    //    cin >> A[i];
    //}

  	bool a=true;//奇数に大文字、偶数に小文字があった時点でNo、他ならYesとなるようにしたい
  	for(int i=0; i<N; i++){//奇数：0から2つ飛ばし、偶数：1から2つ飛ばしの別々のforにするとelseやbreakがうまく使えないので、同じfor内でiを2で割った余りで偶奇を分類する
        if(i%2==0){
        	if(isupper(X[i])){//A[i]うまく入力されてないかもしれない
        		a=false;
          		//break;なくてもいい
        	}
        }
        if(i%2==1){
        	if(islower(X[i])){//A[i]うまく入力されてないかもしれない
        		a=false;
          		//break;なくてもいい
        	}
        }
    }
  	if(a){
    	cout << "Yes" << endl;
    }
    else{
		cout << "No" << endl;
    }
    return 0;
}
