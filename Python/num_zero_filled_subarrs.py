# Simple one pass
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        curr = 0
        total = 0
        for num in nums:
            if num == 0:
                curr += 1
                total += curr
            else:
                curr = 0
        return total

# Two Pointer
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        def sum_to(num):
            return num * (num + 1) // 2

        n = len(nums)
        left = 0
        total = 0
        while left < n:
            if nums[left] == 0:
                right = left + 1
                while right < n and nums[right] == 0:
                    right += 1
                subtotal = right - left
                total += sum_to(subtotal)
                left = right
            left += 1
        return total
