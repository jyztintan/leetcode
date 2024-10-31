from queue import Queue
from typing import List


class Solution:
    memoized = {}
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # If we have enough limit, we can just break all obstacles through the shortest path
        if k >= m + n - 2:
            return m + n - 2

        curr = (0, 0, k)
        q = Queue()
        q.put((0, curr))
        seen = {curr}
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while not q.empty():
            steps, (row, col, k) = q.get()
            if row == m - 1 and col == n - 1:
                return steps

            for x, y in directions:
                new_row, new_col = row + x, col + y
                if (0 <= new_row < m) and (0 <= new_col < n):
                    limit = k - grid[new_row][new_col]
                    curr = (new_row, new_col, limit)
                    if k >= 0 and curr not in seen:
                        seen.add(curr)
                        q.put((steps + 1, curr))
        return -1


grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
print(Solution().shortestPath(grid, 1))

