#include <bits/stdc++.h>
using namespace std;

int main() {
  string str;
  int nop,count=1;
  cin  >> str;
  nop = (str.size()-1)/2;

  for (int i=0;i<nop;i++){
    cout << str.at(i*2+1) << endl;
    if (str.at(i*2+1) == '+'){
      count += 1;
    }else{
      count -= 1;
    }
  }
  
  cout << count << endl;
}
