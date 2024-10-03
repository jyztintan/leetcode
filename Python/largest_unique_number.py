class Solution:
    def largestUniqueNumber(self, nums) -> int:
        seen = set()
        duplicate = set()
        for num in nums:
            if num in seen:
                duplicate.add(num)
            seen.add(num)

        best = -1
        for num in nums:
            if num in duplicate:
                continue
            best = max(best, num)
        return best

