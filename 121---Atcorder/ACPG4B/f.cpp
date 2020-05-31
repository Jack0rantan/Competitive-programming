#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,m;
  cin >> n;

  vector <int> a(n);
  for(int i = 0;i<n;i++){
    cin >> a.at(i);
    m +=a.at(i);
  }
  int ans;
  for(int i = 0;i<n;i++){
    ans = a.at(i)-m/a.size();
    if(ans>0) cout<< ans << endl;
    else cout<< -ans << endl;
  }
}