#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;
  vector<int> d(N);
  for (int i =0;i<N;i++){
  cin >> d.at(i);
  }

  int count = 0;
  for (int i =0;i<N;i++){
    for (int j=0;j<N;j++){
      count += d.at(i)*d.at(j);
    }

  }
  for(int i=0;i<N;i++){
      count -= d.at(i)*d.at(i);
    }
  cout << count/2 << endl;
}
