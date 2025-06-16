class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_diff = -1
        prev_min = float('inf')
        for num in nums:
            if num - prev_min > max_diff and num - prev_min > 0:
                max_diff = num - prev_min
            prev_min = min(prev_min, num)
        return max_diff

