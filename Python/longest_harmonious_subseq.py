class Solution:
    def findLHS(self, nums: List[int]) -> int:
        seen = {}
        best = 0
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            if num + 1 in seen:
                best = max(best, seen[num] + seen[num + 1])
            if num - 1 in seen:
                best = max(best, seen[num] + seen[num - 1])
        return best

