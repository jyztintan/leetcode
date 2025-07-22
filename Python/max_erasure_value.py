class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen, total = set(), 0
        ans = 0
        left = 0
        n = len(nums)
        for right in range(n):
            while nums[right] in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1
            seen.add(nums[right])
            total += nums[right]
            ans = max(ans, total)
        return ans
