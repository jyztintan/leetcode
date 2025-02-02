class Solution:
    def check(self, nums: List[int]) -> bool:
        chance = 1
        for idx in range(len(nums)):
            # This also works when comparing the 0th and -1th index
            if nums[idx] < nums[idx - 1]:
                chance -= 1
                if chance < 0:
                    return False
        return True
