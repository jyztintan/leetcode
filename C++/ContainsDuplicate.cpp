#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int> &nums) {
        unordered_set<int> set;

        for (int num : nums) {
            if (set.find(num) != set.end()) {
                return true;
            }
            set.insert(num);
        }
        return false;
    }
};

int main() {
    Solution solution;
    vector<int> tc1 = {1, 2, 3, 1};
    vector<int> tc2 = {1, 2, 3, 4};
    vector<int> tc3 = {1, 1, 1, 3, 3, 4, 3, 2, 4, 2};
    cout << solution.containsDuplicate(tc1);
    cout << solution.containsDuplicate(tc2);
    cout << solution.containsDuplicate(tc3);
    return 0;
}