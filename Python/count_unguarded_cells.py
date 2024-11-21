from typing import List


class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0] * n for _ in range(m)]

        for r, c in walls:
            matrix[r][c] = 2

        for r, c in guards:
            matrix[r][c] = 2

        for r, c in guards:
            # Check up
            for row in range(r - 1, -1, -1):
                if matrix[row][c] == 2:
                    break
                matrix[row][c] = 1

            # Check down
            for row in range(r + 1, m):
                if matrix[row][c] == 2:
                    break
                matrix[row][c] = 1

            # Check left
            for col in range(c - 1, -1, -1):
                if matrix[r][col] == 2:
                    break
                matrix[r][col] = 1

            # Check right
            for col in range(c + 1, n):
                if matrix[r][col] == 2:
                    break
                matrix[r][col] = 1

        count = 0
        for row in matrix:
            for ele in row:
                if ele == 0:
                    count += 1
        return count


guards = [[0, 0], [1, 1], [2, 3]]
walls = [[0, 1], [2, 2], [1, 4]]
print(Solution().countUnguarded(4, 6, guards, walls))
