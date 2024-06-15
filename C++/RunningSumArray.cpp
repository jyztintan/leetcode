class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        int sum = 0;
        std::vector<int> run_sum;
        for (int i : nums) {
            sum += i;
            run_sum.push_back(sum);
        }
        return run_sum;
    }
};