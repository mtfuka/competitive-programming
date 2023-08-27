#include <bits/stdc++.h>
using namespace std;

int main() {
  int N;
  cin >> N;

  if(N%2==0){
  cout << 0.5 << endl;
  }

  if(N%2==1){
  cout << double ((N+1)/2)/N << endl;
  }
}
