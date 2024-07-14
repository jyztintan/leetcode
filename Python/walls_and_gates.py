import queue

class Solution:
    def islandsAndTreasure(self, grid) -> None:

        def bfs(row, col):

            q = queue.Queue()
            q.put((0, row, col))
            while not q.empty():
                dist, row, col = q.get()
                grid[row][col] = dist

                # BFS Upwards
                if 0 <= row - 1 and dist + 1 < grid[row - 1][col]:
                    q.put((dist + 1, row - 1, col))

                # BFS Downwards
                if row + 1 < len(grid) and dist + 1 < grid[row + 1][col]:
                    q.put((dist + 1, row + 1, col))

                # BFS Left
                if 0 <= col - 1 and dist + 1 < grid[row][col - 1]:
                    q.put((dist + 1, row, col - 1))

                # BFS Left
                if col + 1 < len(grid[0]) and dist + 1 < grid[row][col + 1]:
                    q.put((dist + 1, row, col + 1))

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    bfs(row, col)

        return grid