#include <iostream>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int map[26] = {0};
        if (s.length() != t.length()) {
            return false;
        }
        for (int i = 0; i < s.length(); i++) {
            map[s[i] - 'a']++;
        }
        for (int i = 0; i < t.length(); i++) {
            map[t[i] - 'a']--;
        }
        for (int i = 0; i < 26; i++) {  
            if (map[i] != 0) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    return 0;
}