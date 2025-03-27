# Optimised O(N) time but more elegant
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find dominant ele
        dominant, count = nums[0], 0
        for num in nums:
            if num == dominant:
                count += 1
            else:
                count -= 1
            if count == 0:
                dominant = num
                count = 1

        total_count = nums.count(dominant)

        left_count = 0
        for idx, num in enumerate(nums):
            if num == dominant:
                left_count += 1
                right_count = total_count - left_count
                if left_count * 2 > idx + 1 and right_count * 2 > len(nums) - idx - 1:
                    return idx
        return -1

# Original O(N) Time
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Find dominant ele
        dominant, count = -1, -1
        right_subarr = {}
        for num in nums:
            right_subarr[num] = right_subarr.get(num, 0) + 1
            if count < right_subarr[num]:
                dominant, count = num, right_subarr[num]
        right_len = len(nums)

        left_subarr = {}
        left_len = 0
        for idx, num in enumerate(nums):
            left_subarr[num] = left_subarr.get(num, 0) + 1
            left_len += 1
            right_subarr[num] -= 1
            right_len -= 1
            if num == dominant:
                if left_subarr[num] > left_len // 2 and right_subarr[num] > right_len // 2:
                    return idx
        return -1
