class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for left in range(len(nums) - 2):
            if nums[left] + nums[left + 2] == nums[left + 1] / 2:
                count += 1
        return count
