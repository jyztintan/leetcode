# One pass O(N) time, in-place operations so O(1) space
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        write = 0
        for ptr in range(n):
            if ptr < n - 1 and nums[ptr] and nums[ptr] == nums[ptr + 1]:
                nums[ptr] *= 2
                nums[ptr + 1] = 0
            if nums[ptr] != 0:
                nums[ptr], nums[write] = nums[write], nums[ptr]
                write += 1
        return nums


# O(N) Time, Space
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # Dummy end to avoid index error
        nums.append(0)

        ptr = 0
        n = len(nums)
        ans = []
        while ptr < n - 1:
            # Also check if val != 0
            if nums[ptr] and nums[ptr] == nums[ptr + 1]:
                ans.append(nums[ptr] * 2)
                ptr += 1
            elif nums[ptr]:
                ans.append(nums[ptr])
            ptr += 1

        # Fill in remaining 0s
        while len(ans) != n - 1:
            ans.append(0)

        return ans
