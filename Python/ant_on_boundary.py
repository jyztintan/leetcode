class Solution(object):
    def returnToBoundaryCount(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        curr = 0
        prev = None
        for num in nums:
            curr += num
            if curr == 0:
                count += 1
        return count


nums = [3,2,-3,-4]
print(Solution().returnToBoundaryCount(nums))