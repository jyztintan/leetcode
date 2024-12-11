class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        n = len(nums)
        count = 0
        nums.sort()
        for idx, num in enumerate(nums):
            left = idx + 1
            right = n - 1
            while left < right:
                if num + nums[left] + nums[right] < target:
                    # Choosing any between left and right will pass
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
