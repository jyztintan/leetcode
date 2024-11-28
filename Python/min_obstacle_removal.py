# Solution 1: 0 - 1 BFS
# Since the 'edges' are either 0 or 1 (obstacle or no obstacle) we can do normal BFS for faster time complexity
# But perform the BFS in a binary 'sorted' fashion, by appending heavier operations on the right while appending
# less cost operations to the left of the deque.
# Time complextiy: O(m * n)
from collections import deque


class Solution:
    def minimumObstacles(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        dq = deque()
        dq.append((0, (0, 0)))
        visited = set([(0,0)])

        while dq:
            removed, (row, col) = dq.popleft()
            if row == m - 1 and col == n - 1:
                return removed

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    if grid[new_row][new_col] == 1:
                        dq.append((removed + 1, (new_row, new_col)))
                    else:
                        dq.appendleft((removed, (new_row, new_col)))


import heapq


# Solution 2: Dijkstra, greedily processing the paths with less cost first
# Time complexity: O(m*n log( m*n ) ) as the min heap has a maximum of m * n elements
class Solution:
    def minimumObstacles(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        q = []
        heapq.heappush(q, (0, (0, 0)))

        visited = set([(0, 0)])
        while q:
            removed, (row, col) = heapq.heappop(q)
            if row == m - 1 and col == n - 1:
                return removed

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for x, y in directions:
                if 0 <= row + x < m and 0 <= col + y < n and (row + x, col + y) not in visited:
                    visited.add((row + x, col + y))
                    if grid[row + x][col + y] == 1:
                        heapq.heappush(q, (removed + 1, (row + x, col + y)))
                    else:
                        heapq.heappush(q, (removed, (row + x, col + y)))
