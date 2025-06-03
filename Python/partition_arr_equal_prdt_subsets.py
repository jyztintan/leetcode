# O(N) Elegant one pass - check that each num is a factor and the total product is target ** 2
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        prdt = 1
        for num in nums:
            prdt *= num
            if target % num != 0:
                return False
        return prdt == target ** 2

# O(2^N) Recursive Brute Force
class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        def can_form(target1, target2, nums):
            if len(nums) == 0:
                if target1 == 1 and target2 == 1:
                    return True
                return False
            if target1 % nums[0] != 0 and target2 % nums[0] != 0:
                return False
            return can_form(target1 // nums[0], target2, nums[1:]) or can_form(target1, target2 // nums[0], nums[1:])
        return can_form(target, target, nums)