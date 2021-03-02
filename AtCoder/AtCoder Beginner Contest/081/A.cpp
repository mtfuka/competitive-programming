#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)

int main() {
	string s;//数字ではなく文字列として最初から入力すれば良い
	cin >> s;

	int ans=0;
	if(s[0]=='1') ans++;
    if(s[1]=='1') ans++;
  	if(s[2]=='1') ans++;
  	cout << ans << endl;
}
