class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            new = - int(str(x)[:0:-1])
        else:
            new = int(str(x)[::-1])
        if new < -2 ** 31 or new > 2 ** 31 - 1:
            return 0
        return new