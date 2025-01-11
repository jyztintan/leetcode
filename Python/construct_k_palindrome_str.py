class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        freq = Counter(s)
        not_even = 0
        for c in freq:
            if freq[c] % 2:
                not_even += 1

        return not_even <= k
