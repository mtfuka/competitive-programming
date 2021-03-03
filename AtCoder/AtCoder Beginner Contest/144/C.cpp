#include <bits/stdc++.h>
using namespace std;

int main(){
  long long int N;
  cin >> N;

  long long int ans = 1e18;
  for (long long int i = 1; i*i <= N; i++) {
  if(N%i==0){
      ans = min(ans,N/i +i-2);
  }
  }
  cout << ans << endl;
}
