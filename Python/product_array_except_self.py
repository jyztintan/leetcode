"""
This solution uses the idea that we can combine the product of left, right subarrays
for each element and finally multiply these results to get the product except self.

Time Complexity: O(n)
1. Create answer list - O(n)
2. Loop through elements in array - O(n)

Space Complexity: O(n)
Output array requires a size of n - O(n)
"""


class Solution:
    def productExceptSelf(self, nums):
        zeros = 0
        total = 1
        n = len(nums)
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                total *= num

        ans = [0] * n
        if zeros > 1:
            return ans
        elif zeros == 1:
            ans[nums.index(0)] = total
            return ans

        ans = []
        for num in nums:
            ans.append(total // num)
        return ans


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n
        pre, post = 1, 1
        for i in range(n):
            ans[i] *= pre
            ans[n-i-1] *= post
            pre *= nums[i]
            post *= nums[n-i-1]
        return ans

# sol = Solution()
# nums = [1,2,3,4]
# print(sol.productExceptSelf(nums))
# nums = [-1,1,0,-3,3]
# print(sol.productExceptSelf(nums))
