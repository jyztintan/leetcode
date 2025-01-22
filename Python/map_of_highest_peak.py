class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])

        cells = [[0] * n for _ in range(m)]

        visited = set()
        curr = set()

        for row in range(m):
            for col in range(n):
                if isWater[row][col] == 1:
                    curr.add((row, col))
                    visited.add((row, col))

        height = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while curr:
            next_curr = set()
            for row, col in curr:
                cells[row][col] = height

                for x, y in directions:
                    new_row, new_col = row + x, col + y
                    if (new_row, new_col) not in visited and 0 <= new_row < m and 0 <= new_col < n:
                        visited.add((new_row, new_col))
                        next_curr.add((new_row, new_col))

            curr = next_curr
            height += 1

        return cells
