import heapq


class Solution:
    def minimumTime(self, grid) -> int:
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1

        m, n = len(grid), len(grid[0])

        possible = [(0, (0, 0))]
        time = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        while possible:
            time, (row, col) = heapq.heappop(possible)
            if row == m - 1 and col == n - 1:
                return time
            if (row, col) in visited:
                continue
            visited.add((row, col))
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited:
                    wait = 1 if (grid[new_row][new_col] - time) % 2 == 0 else 0
                    next_time = max(grid[new_row][new_col] + wait, time + 1)
                    heapq.heappush(possible, (next_time, (new_row, new_col)))
        return -1


# print(Solution().minimumTime([[0,2,4],[3,2,1],[1,0,4]]))