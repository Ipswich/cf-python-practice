#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  int t, n;

  cin >> t;

  while (t--){
    cin >> n;
    vector<int> numbers;

    int input;
    while(n--){
      cin >> input;
      numbers.push_back(input);
    }

    sort(numbers.begin(), numbers.end(), greater<int>());
    
    while(numbers.size() > 1){
      int a = numbers.back();
      numbers.pop_back();
      int b = numbers.back();
      numbers.pop_back();

      int mid = (a+b) / 2;
      numbers.push_back(mid);
    }
    cout << numbers[0] << "\n";
  }

  return 0;
}