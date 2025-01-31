class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        island_sizes = defaultdict(int)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            grid[row][col] = island_label
            island_sizes[island_label] += 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                    dfs(new_row, new_col)

        island_label = 2
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    island_label += 1

        biggest = max(island_sizes.values(), default=0)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    visited = set()
                    island = 1

                    for dx, dy in directions:
                        new_row, new_col = row + dx, col + dy
                        if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] not in visited:
                            label = grid[new_row][new_col]
                            island += island_sizes[label]
                            visited.add(label)

                    biggest = max(biggest, island)
        return biggest
