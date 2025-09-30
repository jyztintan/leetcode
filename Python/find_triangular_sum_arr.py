class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            nxt = []
            for i in range(len(nums) - 1):
                nxt.append((nums[i] + nums[i + 1]) % 10)
            nums = nxt
        return nums[0]
