class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        ans = []
        for curr in range(n + m - 1):
            intermediate = []

            row = max(0, curr - n + 1)
            col = min(curr, n - 1)
            while row < m and col > -1:
                intermediate.append(mat[row][col])
                row += 1
                col -= 1

            if curr % 2 == 0:
                ans.extend(intermediate[::-1])
            else:
                ans.extend(intermediate)

        return ans
