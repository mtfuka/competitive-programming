#include <bits/stdc++.h>
using namespace std;

int main(){
  string text;
  cin >> text;

  if(text=="Sunny"){
    cout << "Cloudy" << endl;
  }

  if(text=="Cloudy"){
    cout << "Rainy" << endl;
  }

  if(text=="Rainy"){
    cout << "Sunny" << endl;
  }
}
