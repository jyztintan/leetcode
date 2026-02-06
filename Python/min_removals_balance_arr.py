class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        right = n - 1
        best = 0
        for left in range(n - 1, -1, -1):
            while nums[left] * k < nums[right]:
                right -= 1
            best = max(best, right - left + 1)
        return n - best
