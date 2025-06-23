class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            new = 0
            for c in str(n):
                new += int(c) ** 2
            n = new
        return True
