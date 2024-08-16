class Solution:
    def maxDistance(self, arrays) -> int:
        highest = -float('inf')
        lowest = float('inf')
        best = -float('inf')
        for arr in arrays:
            best = max(best, arr[-1] - lowest, highest - arr[0])
            highest = max(highest, arr[-1])
            lowest = min(lowest, arr[0])
        return best

# arrays = [[1,2,3],[4,5],[1,2,3]]
# print(Solution().maxDistance(arrays))
