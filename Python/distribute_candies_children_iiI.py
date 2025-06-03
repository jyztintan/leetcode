class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def cal(x):
            if x < 0:
                return 0
            return x * (x - 1) // 2

        return cal(n + 2) - 3 * cal(n - limit + 1) + 3 * cal(n - (limit + 1) * 2 + 2) - cal(n - 3 * (limit + 1) + 2)