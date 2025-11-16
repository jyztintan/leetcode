class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10 ** 9 + 7
        curr = 0
        total = 0
        for c in s:
            if c == '1':
                curr += 1
                total = (total + curr) % MOD
            else:
                curr = 0
        return total
