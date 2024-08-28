from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        visited = set()
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid2[row][col] == 0 or (row, col) in visited:
                return
            visited.add((row, col))
            grid2[row][col] = 0
            direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in direction:
                dfs(row + x, col + y)

        # Ignore instances where the there is an island in grid2 but no island in grid1
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    dfs(row, col)

        # All remaining islands in grid2 are sub-islands of grid1, so just count num of islands
        ans = 0
        for row in range(m):
            for col in range(n):
                if grid2[row][col] == 1:
                    ans += 1
                    dfs(row, col)
        return ans

# Not optimised
# class Solution:
#     def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
#         m, n = len(grid1), len(grid1[0])
#
#         visited1 = set()
#
#         def dfs(grid, row, col, visited):
#             if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0 or (row, col) in visited:
#                 return False
#             visited.add((row, col))
#             direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
#             for x, y in direction:
#                 dfs(grid, row + x, col + y, visited)
#             return True
#
#         for row in range(m):
#             for col in range(n):
#                 if grid1[row][col] == 1:
#                     dfs(grid1, row, col, visited1)
#
#         ans = 0
#         visited2 = set()
#         for row in range(m):
#             for col in range(n):
#                 if grid2[row][col] == 1 and (row, col) not in visited2:
#                     island = set()
#                     dfs(grid2, row, col, island)
#                     if island.issubset(visited1):
#                         ans += 1
#                     visited2.update(island)
#         return ans

# grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
# grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
# print(Solution().countSubIslands(grid1, grid2))
