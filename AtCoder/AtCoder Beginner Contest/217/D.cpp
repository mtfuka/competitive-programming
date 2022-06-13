#include <bits/stdc++.h>
using namespace std;

int main() {
    long long l, q;
    cin >> l >> q;
    multiset<long long> st;
    st.insert(0);
    st.insert(l);
    while (q--) {
        int c;
        cin >> c;
        if (c == 1) {
            long long x;
            cin >> x;
            st.insert(x);
        } else {
            long long x;
            cin >> x;
            auto itr2 = st.lower_bound(x);
            auto itr1 = itr2--;
            cout << *itr1 - *itr2 << endl;
        }
    }
}