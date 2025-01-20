class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        rows = [0] * m
        cols = [0] * n

        # Map value to (row, col) location
        locations = {}
        for row in range(m):
            for col in range(n):
                val = mat[row][col]
                locations[val] = (row, col)

        # Iteratively paint and return when there is a full row/col
        for idx, val in enumerate(arr):
            row, col = locations[val]
            rows[row] += 1
            if rows[row] == n:
                return idx
            cols[col] += 1
            if cols[col] == m:
                return idx
