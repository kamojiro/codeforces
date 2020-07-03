#include <iostream>
#include <vector>
#include <cstdio>
#include <string>
#include <algorithm>
#include <climits>
using namespace std;
typedef long long int ll;
#define all(x) x.begin(),x.end()

int main()
{
  int n;
  string l, r;
  cin >> n;
  cin >> l >> r;
  vector<int> V[27];
  vector<string> ANS;
  vector<int> rq;
  for (int i = 0; i < n; ++i) {
    if (l[i] == '?') {
      V[26].push_back(i+1);
    }else {
      V[(int) l[i] - (int)'a'].push_back(i+1);
    }
  }
  for (int i = 0; i < n; ++i) {
    if (r[i] != '?') {
      if (V[(int) r[i] - (int)'a'].size()) {
        ANS.push_back( ((string)V[atoi(r[i]) - atoi('a')].back()) + ' ' + (string)(i+1));
                       V[(int)r[i] - (int)'a'].pop_back());
      }else if (V[26].size()) {
        ANS.push_back( (string)V[26].back() + " " + (string)(i+1));
        V[26].pop_back();
      }else {
        rq.push_back(i+1);
      }
    }
  }
  if (rq.size()) {
    for (int i = 0; i < 27; ++i) {
      while (V[i].size() and rq.size()) {
        ANS.push_back( (string V[i].back() + " " + (string rq.back())));
        V[i].pop_back();
        rq.pop_back();
      }
    }
  }
  cout << ANS.size() << "\n";
  int t = ANS.size();
    for (int i = 0; i < t; ++i) {
      cout << ANS[i] << "\n";
    }
  
  return 0;
}
