# Kadane's Algorithm -> O(n) time

class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]

        highest = nums[0]
        lowest = nums[0]
        ans = nums[0]

        for num in nums[1:]:
            if num < 0:
                highest, lowest = lowest, highest

            highest = max(num, num * highest)
            lowest = min(num, num * lowest)
            ans = max(ans, highest)
        return ans


# print(Solution().maxProduct([2,3,-2,4]))
