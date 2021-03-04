#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int f(int x){//関数作らないとTLEになる
	int sum=0;
    while(x>0){//x>9にすると一番先頭の桁が足されない
    sum+=x%10;
    x/=10;
    }
  	return sum;
}
int main(){
    int N,A,B;
    cin >> N >> A >> B;
  	int ans=0;
	rep(i,N+1){
      	if(A<=f(i) && f(i)<=B) ans+=i;
    }
  	cout << ans << endl;
    return 0;
}
