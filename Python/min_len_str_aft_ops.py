class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)

        remainder = 0
        for c in freq:
            if freq[c] % 2:
                remainder += 1
            else:
                remainder += 2
        return remainder
