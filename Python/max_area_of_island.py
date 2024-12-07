# Thank you Prof Halim for teaching UFDS during my time in CS2040S AY23/24 Semester 1
# Source: https://github.com/stevenhalim/cpbook-code/blob/master/ch2/ourown/unionfind_ds.py
# Modified variable naming for code readability
class UFDS:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.num_disjoint_sets = n

    def find(self, element):
        children = []
        while element != self.parents[element]:
            children.append(element)
            element = self.parents[element]
        for child in children:
            self.parents[child] = element
        return element

    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        # If they already have the same parent, then this union is "redundant"
        if root_a == root_b:
            return True

        if self.ranks[root_a] < self.ranks[root_b]:
            self.parents[root_a] = root_b
        elif self.ranks[root_b] < self.ranks[root_a]:
            self.parents[root_b] = root_a
        else:
            self.parents[root_b] = root_a
            self.ranks[root_a] += 1

        self.num_disjoint_sets -= 1


class Solution:
    def maxAreaOfIsland(self, grid) -> int:

        # Number of rows
        m = len(grid)

        # Number of columns
        n = len(grid[0])

        # Instantiate a UFDS, representing each point in the matrix
        ufds = UFDS(m*n)

        # Keep track of number of points that are water
        for row in range(m):
            for col in range(n):

                # If this point is land
                if grid[row][col] == 1:

                    # We connect this land with the land directly below (if any)
                    if row + 1 < m and grid[row + 1][col] == 1:
                        ufds.union(row * n + col, (row + 1) * n + col)
                    # We connect this land with the land directly to the right (if any)
                    if col + 1 < n and grid[row][col + 1] == 1:
                        ufds.union(row * n + col, row * n + col + 1)


        # For each unique parents which will represent 'islands', we count its area
        areas = {}
        for row in range(m):
            for col in range(n):
                # We relax all the points so that all connected points (ie islands) will have the same parent
                # If this point is land
                if grid[row][col] == 1:
                    parent = ufds.find(row * n + col)
                    areas[parent] = areas.get(parent, 0) + 1

        # Subtract the number of water points in our UFDS
        if areas.values():
            ans = max(areas.values())
            return ans
        return 0

# Recursive
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = set()

        def explore_island(row, col):
            if (row, col) in seen or row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == 0:
                return 0
            seen.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            count = 1
            for x, y in directions:
                new_row, new_col = row + x, col + y
                count += explore_island(new_row, new_col)
            return count

        best = 0
        for row in range(m):
            for col in range(n):
                best = max(best, explore_island(row, col))
        return best

# Iterative
class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        biggest = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    #Start dfs
                    st = [(row, col)]
                    visited = set()
                    while st:
                        x, y = st.pop()
                        if (x, y) in visited:
                            continue
                        grid[x][y] = 0
                        visited.add((x, y))
                        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                        for dx, dy in directions:
                            new_row, new_col = dx + x, dy + y
                            if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == 1:
                                st.append((new_row, new_col))
                    biggest = max(biggest, len(visited))
        return biggest

# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
# print(Solution().maxAreaOfIsland(grid))