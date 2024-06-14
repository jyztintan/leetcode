"""
This solution first sorts the nums array, then checks that each subsequent element is strictly greater than the one before.
If not, we find the minimum increment needed to make it greater, and accumulate these increments to find our final answer.

Time Complexity: O(nlogn + n) = O(nlogn)
1. Sort the nums array - O(nlogn)
2. Loop through array to count total increments - O(n)

Space Complexity: O(n)
Nums array - O(n)
"""

class Solution:
    def minIncrementForUnique(self, nums):
        nums.sort()
        ans = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                increment = nums[i - 1] - nums[i] + 1
                ans += increment
                nums[i] += increment
        return ans

"""
This solution follows the counting method and buckets our values in the nums array.
We then iterate through the buckets, keeping track of the excess duplicates and increment/decrement accordingly.
After going through the buckets, we still need to account for values that extend beyond the max values.

Time Complexity: O(max(nums) + n + max(nums) + n) = O(n + max(nums))
1. Create buckets - O(max(nums))
2. Loop through array to bucket values - O(n)
3. Loop through buckets - O(max(nums))
4. Continue for excess values - O(n)

Space Complexity: O(max(nums))
1. Nums array - O(n)
2. Frequency count array - O(max(nums))
"""
class Solution:
    def minIncrementForUnique(self, nums):
        max_num = max(nums)
        buckets = [0] * (max_num + 1)
        for num in nums:
            buckets[num] += 1
        ans = 0
        excess = 0
        for bucket in buckets:
            excess += bucket - 1
            excess = max(0, excess)
            ans += excess
        while excess:
            ans += excess - 1
            excess -= 1
        return ans

# sol = Solution()
# nums = [1,2,2]
# print(sol.minIncrementForUnique(nums))
# nums = [3,2,1,2,1,7]
# print(sol.minIncrementForUnique(nums))
# nums = [2,2,2,2,0]
# print(sol.minIncrementForUnique(nums))