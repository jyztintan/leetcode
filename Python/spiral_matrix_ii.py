from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        grid = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        curr = 1

        while left <= right and top <= bottom:
            # Fill top row:
            for i in range(left, right + 1):
                grid[top][i] = curr
                curr += 1
            top += 1
            # Fill right-most col
            for i in range(top, bottom + 1):
                grid[i][right] = curr
                curr += 1
            right -= 1
            # Fill bottom row, provided it is still valid
            if bottom >= top:
                for i in range(right, left - 1, -1):
                    grid[bottom][i] = curr
                    curr += 1
                bottom -= 1
            # Fill left-most row, if it is still valid
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    grid[i][left] = curr
                    curr += 1
                left += 1
        return grid



