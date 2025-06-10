class Solution:
    def maxDifference(self, s: str) -> int:
        odd = 0
        even = float('inf')
        freq = Counter(s)
        for c, count in freq.items():
            if count % 2:
                odd = max(odd, count)
            else:
                even = min(even, count)
        return odd - even
