class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = nums[0]
        count = 1
        for num in nums:
            if start + k < num:
                start = num
                count += 1
        return count
