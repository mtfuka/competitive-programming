#include <bits/stdc++.h>
using namespace std;

int main(){
  int N;
  cin >> N;

  bool a = true;

  for (int i = 1; i < 10; i++) {
  if(N%i==0&&1<=N/i&&N/i<=9){
      a=false;
        cout << "Yes" << endl;
    break;
  }
  }


  if(a){
  cout << "No" << endl;
  }

}
