class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        diff = float('inf')
        for low, num in enumerate(nums):
            left, right = low + 1, n - 1
            while left < right:
                check_sum = num + nums[left] + nums[right]
                if abs(check_sum - target) < abs(diff):
                    diff = check_sum - target
                if check_sum < target:
                    left += 1
                else:
                    right -= 1
            if diff == 0:
                return target
        return target + diff
