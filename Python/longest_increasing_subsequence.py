class Solution:
    def lengthOfLIS(self, nums) -> int:
        # Initially, the longest subsequence is just the number itself
        ans = [1] * len(nums)

        # For each number, we check if it can be added to previous subsequences
        for i in range(len(nums)):
            # Each number before this has been processed, so we take the longest subsequence out of these
            # Then we append the current number to the longest subsequence to get an even longer subsequence
            for j in range(i):
                # Check that the number can be added to the subsequence
                if nums[i] > nums[j]:
                    # Check that the new subsequence is the longest
                    ans[i] = max(ans[i], ans[j] + 1)
        return max(ans)

# nums = [10,9,2,5,3,7,101,18]
# print(Solution().lengthOfLIS(nums))
