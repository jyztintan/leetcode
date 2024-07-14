import queue

class Solution:
    def orangesRotting(self, grid) -> int:
        q = queue.Queue()
        fresh = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.put((0, row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        if not fresh:
            return 0

        ans = 0

        while not q.empty():
            dist, row, col = q.get()
            ans = max(ans, dist)


            # BFS Upwards
            if 0 < row  and grid[row - 1][col] == 1:
                q.put((dist + 1, row - 1, col))
                grid[row - 1][col] = 2
                fresh -= 1


            # BFS Downwards
            if row + 1 < len(grid) and grid[row + 1][col] == 1:
                q.put((dist + 1, row + 1, col))
                grid[row + 1][col] = 2
                fresh -= 1

            # BFS Left
            if 0 < col and grid[row][col - 1] == 1:
                q.put((dist + 1, row, col - 1))
                grid[row][col - 1] = 2
                fresh -= 1

            # BFS Left
            if col + 1 < len(grid[0]) and grid[row][col + 1] == 1:
                q.put((dist + 1, row, col + 1))
                grid[row][col + 1] = 2
                fresh -= 1

        return ans if not fresh else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
print(Solution().orangesRotting(grid))