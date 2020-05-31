#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;
    vector<int> a(10010);
    vector<int> dp(10010);
    dp[0] = 0;

    cin >> n;
    for (int i = 0 ; i < n ; ++i) cin >> a.at(i);

    for (int i = 0 ; i < n ; ++i){
        dp.at(i+1) = max(dp.at(i), dp.at(i) + a.at(i));
    }

    cout << dp.at(n) << endl;
}