# Math Arithmetic Progression
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n + 1) // 2 - n // m * m * (n // m + 1)

# One loop traversal
# Time: O(N)
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for num in range(1, n + 1):
            if num % m:
                num1 += num
            else:
                num2 += num
        return num1 - num2
