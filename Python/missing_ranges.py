class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        ans = []
        curr = lower
        for num in nums:
            if num > curr:
                ans.append([curr, num - 1])
            curr = num + 1
        if curr <= upper:
            ans.append([curr, upper])
        return ans
