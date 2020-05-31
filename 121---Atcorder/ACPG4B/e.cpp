#include <bits/stdc++.h>
using namespace std;

int main(){
  int h,w;
  cin >> h >> w;
  
  vector<string> board(50);

  for (int i=0;i<h;++i) cin >> board.at(i);

  const vector<int> dx = {1,0,-1,0,1,-1,-1,1};
  const vector<int> dy = {0,1,0,-1,1,1,-1,-1};
  
  for (int i=0;i<h;++i){
    for (int j=0;j<w;++j){
      if (board.at(i).at(j)== '#') continue;

      int n = 0;
      for (int d=0;d<8;++d){
        const int ni = i + dy.at(d);
        const int nj = j + dx.at(d);

        if (ni < 0 or h <= ni) continue;
        if (nj < 0 or w <= nj) continue;
        if (board.at(ni).at(nj) == '#') n++;
      }
      
      board.at(i).at(j) = char(n + '0');

    }
  }
  
  for (int i=0;i<h;++i) cout << board[i] << endl;
}