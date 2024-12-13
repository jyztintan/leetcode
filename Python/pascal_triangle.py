class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        start = self.generate(numRows - 1)
        last_row = start[-1]
        new_row = []
        for idx in range(numRows - 2):
            new_row.append((last_row[idx] + last_row[idx + 1]))
        new_row = [1] + new_row + [1]
        start.append(new_row)
        return start
