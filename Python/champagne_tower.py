# DP solution -> 'collates' all champagne for each glass then simulate overflow
# Time Complexity: O(R^2)
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        tower = [[0] * row for row in range(1, 102)]
        tower[0][0] = poured
        for row in range(query_row + 1):
            for col in range(row + 1):
                overflow = (tower[row][col] - 1) / 2
                if overflow > 0:
                    tower[row + 1][col] += overflow
                    tower[row + 1][col + 1] += overflow

        return min(tower[query_row][query_glass], 1)

# TLE -> grows exponentially because each overflow triggers to 2 more recursive calls
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        res = defaultdict(float)

        def pour(amt, row, col):
            # print(amt, row, col)
            if row > query_row:
                return
            res[(row, col)] += amt
            if res[(row, col)] > 1:
                overflow = (res[(row, col)] - 1) / 2
                res[(row, col)] = 1
                pour(overflow, row + 1, col)
                pour(overflow, row + 1, col + 1)

        pour(poured, 0, 0)
        return res.get((query_row, query_glass), 0)

