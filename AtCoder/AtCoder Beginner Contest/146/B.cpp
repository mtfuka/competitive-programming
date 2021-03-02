#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;
  string S;
  cin >> S;

  for (int i = 0; i < S.size() ; i++){
    S.at(i) += N;
    if(S.at(i)>'Z')
      S.at(i) -= 26;
    }
  cout << S << endl;
}
