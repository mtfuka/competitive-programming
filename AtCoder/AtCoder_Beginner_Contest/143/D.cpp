#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> S(N);
  for (int i=0;i<N;i++){
    cin >> S.at(i);
  }

  sort(S.begin(),S.end());
  int count = 0;
  for (int i=0;i<N;i++){
    for (int j=i+1;j<N;j++){
      for (int k=j+1;k<N;k++){
        if ( S.at(k)<S.at(j)+S.at(i))
      count++;
      }
    }
  }

  cout << count << endl;
  }
