class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        top_k = sorted(list(nums))[-k:]
        freq = {}
        for num in top_k:
            freq[num] = freq.get(num, 0) + 1
        ans = []
        for num in nums:
            if freq.get(num, 0):
                ans.append(num)
                freq[num] -= 1
        return ans
