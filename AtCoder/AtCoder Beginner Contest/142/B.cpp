#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,K;
  cin >> N >> K;
  vector<int> vec(N);
  for (int i = 0; i < N; i++) {
    cin >> vec.at(i);
  }

  int counter = 0;
  for (int i = 0; i < N; i++) {
    if(vec.at(i)>=K)
      counter++;
  }

  cout << counter <<endl;

}
