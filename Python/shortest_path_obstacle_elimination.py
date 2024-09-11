from queue import Queue
from typing import List


class Solution:
    memoized = {}
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        shortest = {}
        q = Queue()
        q.put((0, 0, 0, 0))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while not q.empty():
            row, col, encountered, path = q.get()
            if encountered <= k and path < shortest.get((row, col, encountered), float('inf')):
                shortest[(row, col, encountered)] = path

                path += 1
                for x, y in directions:
                    new_row, new_col = row + x, col + y
                    if 0 <= new_row < m and 0 <= new_col < n:
                        if grid[new_row][new_col] == 0:
                            q.put((new_row, new_col, encountered, path))
                        elif encountered + 1 <= k:
                            q.put((new_row, new_col, encountered + 1, path))
        ans = float('inf')
        for i in range(k + 1):
            if (m - 1, n - 1, i) in shortest:
                ans = min(ans, shortest[(m - 1, n - 1, i)])
        return ans if ans != float('inf') else -1

# grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]]
# grid = [[0,1,1],[1,1,1],[1,0,0]]
# grid = [[0]]
# print(Solution().shortestPath(grid, 1))

