class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        ans = 0
        for num in nums:
            if num - 1 not in s:
                count = 0
                while num + count in s:
                    count += 1
                ans = max(ans, count)
        return ans

s = Solution()
nums = [100,4,200,1,3,2]
print(s.longestConsecutive(nums))

nums = [0,3,7,2,5,8,4,6,0,1]
print(s.longestConsecutive(nums))
