
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        for idx in range(n - 1):
            if nums[idx] % 2 == nums[idx + 1] % 2:
                return False
        return True
