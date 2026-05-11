class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            for c in str(num):
                ans.append(int(c))
        return ans

