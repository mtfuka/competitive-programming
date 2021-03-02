#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int64_t N;//10^10なのでint型(10^-9~10^9)には収まらない
    cin >> N;
  	unordered_set<int64_t> s;//HashSetで数を管理できる、bの約数の個数で重複する個数を場合分けすると考えたがそれは大変そう
  	for (int64_t a = 2; a*a <= N; a++) {//a <= NだとTLEなのでa*a <= Nと節約する
      int64_t x=a*a;//a*=a;とすると増やしていくaと被ってしまうので違う文字を用意する
      while(x<=N){//bもループさせるとTLEになるので、whileで必要な分だけ回す
        s.insert(x);//insertするときに重複を取り除いてくれる
        x*=a;
        //if (1<=a && a<= N) s.insert(x);whileの条件と同じなので要らない
      }
    }

    cout << N-s.size() << endl;//.size()でHashSetの中身を取り出せる
    return 0;
}
