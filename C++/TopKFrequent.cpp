class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> m;
        for (auto num : nums) {
            m[num]++;
        }

        vector<vector<int>> buckets(n+1);

        for (auto pair : m) {
            buckets[pair.second].push_back(pair.first);
        }

        vector<int> ans;

        for (int i = n; i > 0; i--) {
            if (ans.size() >= k) {
                break;
            }
            if (!buckets[i].empty()) {
                ans.insert(ans.end(), buckets[i].begin(), buckets[i].end());
            }
        }
        return ans;
    }
};