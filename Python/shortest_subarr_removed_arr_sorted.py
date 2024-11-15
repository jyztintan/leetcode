class Solution:
    def findLengthOfShortestSubarray(self, arr) -> int:
        n = len(arr)
        if n == 1:
            return 0
