class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # Find starting point
        for row in range(m):
            for col in range(n):
                if grid[row][col] == '*':
                    q.append((row, col, 0))
                    break

        # BFS to get shortest path to food
        while q:
            row, col, steps = q.popleft()
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n:
                    if grid[new_row][new_col] == '#':
                        return steps + 1
                    elif grid[new_row][new_col] == 'O':
                        q.append((new_row, new_col, steps + 1))
                        grid[new_row][new_col] = '*'
        return -1
