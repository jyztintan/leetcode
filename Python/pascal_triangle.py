class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        curr = [[1], [1, 1]]
        for _ in range(2, numRows):
            new_row = [1]
            prev = curr[-1]
            for i in range(len(prev) - 1):
                new_row.append(prev[i] + prev[i + 1])
            new_row.append(1)
            curr.append(new_row)
        return curr


# Recursive but space complexity does not seem ideal since the increasing tree is returned after every recyrsiion
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
