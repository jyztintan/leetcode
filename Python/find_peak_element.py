# Cleaned up and more elegant
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left

# O(logn) solution but need to handle edge cases for len(nums) < 3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1

        while left < right:
            mid = (left + right) // 2
            if (mid == 0 and nums[mid] > nums[1]) or (mid == n - 1 and nums[mid] > nums[mid - 1]) or (
                    nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]):
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            else:
                left = mid + 1
        return left
