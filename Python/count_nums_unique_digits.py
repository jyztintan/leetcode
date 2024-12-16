class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 10

        multiplier = 9
        for i in range(11 - n, 10):
            multiplier *= i

        return multiplier + self.countNumbersWithUniqueDigits(n - 1)
