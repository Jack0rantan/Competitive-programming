#include <bits/stdc++.h>
using namespace std;

int main(){
  int n,m;
  cin >> n >> m;
  
  vector <int> from(m);
  vector <int> to(m);
  vector <int> town(n);

  for(int i = 0;i<m;i++){
    cin >> from.at(i);
    cin >> to.at(i);
    town.at(from.at(i)-1) += 1;
    town.at(to.at(i)-1) += 1;
  }
  for(int i = 0;i<n;i++){
    cout << town.at(i) << endl;
  }
}