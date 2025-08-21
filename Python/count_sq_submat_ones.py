# Bottom up solution with space optimisation
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [0] * n
        ans = 0
        for i in range(m):
            new_dp = [0] * n
            for j in range(n):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        new_dp[j] = 1
                    else:
                        new_dp[j] = 1 + min(dp[j], new_dp[j-1], dp[j-1])
                    ans += new_dp[j]
            dp = new_dp
        return ans

# Bottom up solution treat the top left as the bottom right
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[0] * n for _ in range(m)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    ans += dp[i][j]
        return ans


# Top down solution
class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        dp = [[-1] * n for _ in range(m)]

        def find(row, col):
            if row == m or col == n or mat[row][col] == 0:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            dp[row][col] = 1 + min(find(row + 1, col + 1), find(row + 1, col), find(row, col + 1))
            return dp[row][col]

        ans = 0
        for row in range(m):
            for col in range(n):
                ans += find(row, col)
        return ans

