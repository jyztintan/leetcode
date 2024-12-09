class Solution:
    def __init__(self):
        self.memo = {0:1, 1:1, 2:2}
    def climbStairs(self, n: int) -> int:
        if n in self.memo:
            return self.memo[n]
        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2
        for step in range(2, n):
            ways[step] = ways[step - 1] + ways[step - 2]
        return ways[n - 1]
