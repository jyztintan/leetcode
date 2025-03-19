class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for ptr in range(len(nums) - 2):
            if not nums[ptr]:
                nums[ptr] = 1
                nums[ptr + 1] = 0 if nums[ptr + 1] else 1
                nums[ptr + 2] = 0 if nums[ptr + 2] else 1
                flips += 1

        if not nums[ptr + 1] or not nums[ptr + 2]:
            return -1
        return flips
