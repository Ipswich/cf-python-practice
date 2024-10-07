#include <iostream>
using namespace std;

int main(){
  int t, a, b, c, r(0);
  cin >> t;

  while (t--){
    scanf("%d %d %d", &a, &b, &c);
    if ((a + b + c) >= 2){
      r += 1;
    }
  }
  cout << r << "\n";

  return 0;
}