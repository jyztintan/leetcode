class Solution:
    def minSwaps(self, s: str) -> int:
        close = 0
        open = 0
        swap = 0
        for c in s:
            if c == '[':
                open += 1
                continue
            if close < open:
                close += 1
            else:
                open += 1
                swap += 1
        return swap
