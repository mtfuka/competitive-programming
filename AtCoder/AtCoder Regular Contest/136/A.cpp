#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N;
    cin >> N;
    
    string S;
    cin >> S;

    for (int i = 0; i < N-1; i++){
        if(S[i]=='B'&&S[i+1]=='A'){
        	S[i]='A';
            S[i+1]='B';
        }
      	else if(S[i]=='B'&&S[i+1]=='B'){
        	S[i]='A';
            S.erase(i+1, 1);
            N--;
        }
    }
    
    cout << S << endl;
    return 0;
}