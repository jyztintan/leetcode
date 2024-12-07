class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        result = [[0] * n for _ in range(m)]

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if (row, col) in visited:
                return
            visited.add((row, col))
            result[row][col] += 1
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n and heights[row][col] <= heights[new_row][new_col]:
                    dfs(new_row, new_col)

        # Pacific
        visited = set()
        for col in range(n):
            dfs(0, col)
        for row in range(m):
            dfs(row, 0)

        # Atlantic
        visited = set()
        for col in range(n):
            dfs(m - 1, col)
        for row in range(m):
            dfs(row, n - 1)

        flow = []
        for row in range(m):
            for col in range(n):
                if result[row][col] == 2:
                    flow.append((row, col))
        return flow