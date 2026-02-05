class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i, delta in enumerate(nums):
            idx = (i + delta) % n
            res.append(nums[idx])
        return res
