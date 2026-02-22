class Solution:
    def binaryGap(self, n: int) -> int:
        binary = f"{n:b}"
        best = 0
        prev = inf
        for i, bit in enumerate(binary):
            if bit == '1':
                best = max(best, i - prev)
                prev = i
        return best
