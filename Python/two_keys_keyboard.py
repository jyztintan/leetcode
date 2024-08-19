class Solution:
    def get_highest_factor(self, n):
        highest_factor = 0
        for i in range(n // 2, 1, -1):
            if n % i == 0:
                highest_factor = i
                break
        return highest_factor

    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        # The only way to get prime numbers of n is to copy when only one 'A' and paste n - 1 times
        highest_factor = self.get_highest_factor(n)
        if highest_factor == 0:
            return n

        return self.minSteps(highest_factor) + (n // highest_factor)

print(Solution().minSteps(6))
