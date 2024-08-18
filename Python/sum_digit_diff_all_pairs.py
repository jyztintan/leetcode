class Solution:
    def sumDigitDifferences(self, nums) -> int:
        n = len(nums)
        nums = list(map(str, nums))
        m = len(nums[0])
        ans = 0
        for i in range(m):
            freq = {}
            for num in nums:
                freq[num[i]] = freq.get(num[i], 0) + 1
            if len(freq) == 1:
                continue
            curr = 0
            for key in freq:
                curr += freq[key]
                ans += (n - curr) * freq[key]
        return ans

nums = [13,23,12]
print(Solution().sumDigitDifferences(nums))
nums = [50,28,48]
print(Solution().sumDigitDifferences(nums))

