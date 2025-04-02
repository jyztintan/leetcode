# Iterative solution
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)
        for ptr in range(n - 1, -1, -1):
            points, skip = questions[ptr]
            if ptr + skip + 1 < n:
                points += dp[ptr + skip + 1]
            dp[ptr] = max(points, dp[ptr + 1])
        return dp[0]

# Recursive Solution
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [-1] * n
        def get_points(ptr):
            if ptr >= n:
                return 0
            if dp[ptr] != -1:
                return dp[ptr]
            earned, skip = questions[ptr]
            dp[ptr] = max(get_points(ptr + 1), earned, earned + get_points(ptr + skip + 1))
            return dp[ptr]
        return get_points(0)
