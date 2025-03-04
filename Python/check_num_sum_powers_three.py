class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        possible = []
        for power in range(17):
            possible.append(3 ** power)
        possible.reverse()

        for num in possible:
            if n >= num:
                n -= num

        return n == 0
