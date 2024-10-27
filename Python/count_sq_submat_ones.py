class Solution:
    def countSquares(self, matrix) -> int:
        m = len(matrix)
        n = len(matrix[0])
        memoize = {}

        def count(row, col):
            if row == m or col == n or not matrix[row][col]:
                return 0
            if (row, col) in memoize:
                return memoize[(row, col)]
            memoize[(row, col)] = 1 + min(count(row + 1, col), count(row + 1, col + 1), count(row, col + 1))
            return memoize[(row, col)]

        ans = 0
        for row in range(m):
            for col in range(n):
                ans += count(row, col)
        return ans
