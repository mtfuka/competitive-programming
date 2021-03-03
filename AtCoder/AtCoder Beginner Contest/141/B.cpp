#include <bits/stdc++.h>
using namespace std;

int main(){
  string text;
  cin >> text;

  for(int i=0;i<text.size();i++){

    if(i%2==0){
      if(!(text[i]=='R'||text[i]=='U'||text[i]=='D')){
        cout << "No" << endl;
        return 0;
      }
    }
     if(i%2==1){
      if(!(text[i]=='L'||text[i]=='U'||text[i]=='D')){
        cout << "No" << endl;
        return 0;
      }
       }
  }
cout << "Yes" << endl;
}
