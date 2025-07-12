# Smart Cache: Each query takes O(1) time
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.cumulative = [[0] * (n + 1) for _ in range(m + 1)]
        for row in range(m):
            for col in range(n):
                self.cumulative[row + 1][col + 1] = self.cumulative[row][col + 1] + self.cumulative[row + 1][col] - \
                                                    self.cumulative[row][col] + matrix[row][col]
        print(self.cumulative)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.cumulative[row2 + 1][col2 + 1] - self.cumulative[row1][col2 + 1] - self.cumulative[row2 + 1][col1] + \
            self.cumulative[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# Cache rows: Each query takes O(M) time
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix_rows = []
        for row in range(m):
            new_row = []
            curr = 0
            for col in range(n):
                curr += matrix[row][col]
                new_row.append(curr)
            self.prefix_rows.append(new_row)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for row in range(row1, row2 + 1):
            left = self.prefix_rows[row][col1 - 1] if col1 > 0 else 0
            total += self.prefix_rows[row][col2] - left
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)