#include <bits/stdc++.h>
using namespace std;

int main(){
  int h,w;
  cin >> h >> w;
  
  vector <string> v1(h);

  for(int i = 0;i<h;i++){
    cin >> v1.at(i);
  }

  for (int i = 0 ; i < h+2; i++){
    if(i==0 || i==h+1) cout << string(w+2,'#')<< endl;
    else cout << '#' + v1.at(i-1) + '#' << endl;
  }
}