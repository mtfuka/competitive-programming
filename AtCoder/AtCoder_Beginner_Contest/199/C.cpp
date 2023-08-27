#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int N;
    cin >> N;
    string S;
    cin >> S;
    string S1 = S.substr(0,N);
    string S2 = S.substr(N);
    int Q;
    cin >> Q;
    rep(i,Q){
    	int T,A,B;
        cin >> T >> A >> B;
        if(T==1){
        	if(A-1<N&&B-1<N) swap(S1[A-1],S1[B-1]);
            else if(N<=A-1&&N<=B-1) swap(S2[A-N-1],S2[B-N-1]);
            else swap(S1[A-1],S2[B-N-1]);
            
        }
        if(T==2){
        	swap(S1,S2);
        }
    }
    
    cout << S1 << S2 << endl;
    return 0;
}