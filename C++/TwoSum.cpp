#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> m;
        int n=nums.size();
        for(int i=0;i<n;i++){
            int ans=target-nums[i];
            if(m.find(ans)!=m.end()){
                 return {m[ans],i};
            }
            m[nums[i]]=i;
        }
        return {-1,-1};
    }
};

// Main Function
int main() {
    Solution solution;
    std::vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = solution.twoSum(nums, target);

    if (!result.empty()) {
        std::cout << "Indices: " << result[0] << " and " << result[1] << std::endl;
    } else {
        std::cout << "No valid two sum solution found." << std::endl;
    }

    return 0;
}