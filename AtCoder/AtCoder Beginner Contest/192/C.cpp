#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)
#define rep2(i, s, n) for (int i = s; i < n; i++)

int N, K;

int f(int x) {//関数f(x)の定義
    string s = to_string(x);//to_stringで数を文字列に変換、数字のままだとsortできないので文字列にする

  	sort(s.begin(),s.end());//文字列sを昇順にsort、sort(s.begin(),s.end())で最初から最後まで並び替え
    int g2 = stoi(s);//stoi関数：文字列を整数に変換、先頭の0も上手く処理してくれる

    sort(s.begin(),s.end(), greater<char>());//文字列sを降順にsort、greater<>()を入れると降順(逆順)にsortできる
    int g1 = stoi(s);//文字列を整数に戻す

    return g1 - g2;//関数の返り値はreturn文を使う
}

int main() {//main関数から処理は始まる
    cin >> N >> K;
    int a = N;//初項a0=N
    rep(i, K) a = f(a);//k回関数f(x)を実行する
    cout << a << endl;
}
