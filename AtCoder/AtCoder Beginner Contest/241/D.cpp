#include <bits/stdc++.h>
using namespace std;

int main() {
    int q;
    cin >> q;
    multiset<long long> st;
    while (q--) {
        int t;
        cin >> t;
        if (t == 1) {
            long long x;
            cin >> x;
            st.insert(x);
        } else if (t == 2) {
            long long x, k;
            cin >> x >> k;
            auto itr = st.upper_bound(x);
            bool ok = true;
            while (k--){           
                if (itr==st.begin()){
                    ok = false;
                    break;
                }
                itr--;
            }
            if (ok) cout << *itr << endl;
            else cout << -1 << endl;
        } else {
            long long x, k;
            cin >> x >> k;
            auto itr = st.lower_bound(x);
            bool ok = true;
            k--;
            while (k--){
                if (itr==st.end()){
                    ok = false;
                    break;
                }
                itr++;
            }
            if (ok&&itr!=st.end()) cout << *itr << endl;
            else cout << -1 << endl;
        }
    }
}