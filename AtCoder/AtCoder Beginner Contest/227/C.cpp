#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
  long long N;
  cin >> N;
    
  long long ans=0;
  for (long long A = 1; A*A*A <= N; A++){
    for (long long B = A; B*B <= N/A; B++){
      ans += N/A/B-B+1;
    }
  }
    
  cout << ans << endl;
  return 0;
}