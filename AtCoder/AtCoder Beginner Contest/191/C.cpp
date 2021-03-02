#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < n; i++)

int main(){
    int H,W;
    cin >> H >> W;
    vector<vector<char>> A(H,vector<char>(W));
    rep(i, H) {
        rep(j, W){
        cin >> A[i][j];
        }
    }
  	int ans=0;
  	//(x,y)の周囲4マスの#の数をカウントする
  	int a=0;
  	//-1しないとマスが定義されていない下側と右側までカウントしようとしてエラーになる
  	//周の端は.であることが保証されているので数えなくてよい
  	rep(x, H-1){
        rep(y, W-1){
        if(A[x][y]=='#'){a++;}
        if(A[x+1][y]=='#'){a++;}
        if(A[x][y+1]=='#'){a++;}
        if(A[x+1][y+1]=='#'){a++;}
        //#のカウント数が1or3ならばカウントする
        if(a==1||a==3){ans++;}
        a=0;
        }
    }
    cout << ans << endl;
    return 0;
}
