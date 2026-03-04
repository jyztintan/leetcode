class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = [0] * m
        cols = [0] * n
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1:
                    rows[row] += 1
                    cols[col] += 1
        count = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 1 and rows[row] == 1 and cols[col] == 1:
                    count += 1
        return count
