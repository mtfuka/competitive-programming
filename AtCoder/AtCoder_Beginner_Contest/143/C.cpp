#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<char> S(N);
  for (int i=0;i<N;i++){
    cin >> S.at(i);
  }

  int count =N;
  for (int i=1;i<N;i++){
    if ( S.at(i) == S.at(i-1))
      count--;
  }

  cout << count << endl;
  }
