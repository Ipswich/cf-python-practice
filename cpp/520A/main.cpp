#include <iostream>
#include <vector>
using namespace std;

int main(){
  int t;
  string s;
  cin >> t;
  cin >> s;
  vector<bool> checkList(26, false);

  int index;

  for (int i = 0; i < s.length(); i++){
    if('A' <= s[i] && s[i] <= 'Z'){
      index = s[i] - 'A';
    }
    else if ('a' <= s[i] && s[i] <= 'z'){
      index = s[i] - 'a';
    } else {
      continue;
    }
    checkList[index] = true;
  }

  for (int i = 0; i < 26; i++){
    if (checkList[i] != true){
      cout << "NO" << "\n";
      return 0;
    }
  }

  cout << "YES" << "\n";

  return 0;
}