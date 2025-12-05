class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        count = 0
        for num in nums[:-1]:
            left += num
            right -= num
            if right % 2 == left % 2:
                count += 1
        return count
