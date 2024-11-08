class Solution:
    def getMaximumXor(self, nums, maximumBit: int):
        curr = 0
        ans = []
        for num in enumerate(nums):
            curr ^= num
            # Create bit mask to flip curr and get the first maximumBit bits
            ans.append(~curr & ((1 << maximumBit) - 1))
        return ans
