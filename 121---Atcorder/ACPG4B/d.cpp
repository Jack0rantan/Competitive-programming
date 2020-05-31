#include <bits/stdc++.h>
using namespace std;

int main() {
  int N,count=0,mean;
  cin >> N;
  
  vector <int> vec(N);
  for(int i=0;i<N;i++){
    cin >> vec.at(i);
    count += vec.at(i);
  }
  
  mean = count / vec.size();
  for(int i=0;i<vec.size();i++){
    cout <<vec.at(i)-mean << endl;
  }
}
