class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def explore_island(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] == "0":
                return

            grid[row][col] = "0"
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                new_row, new_col = row + x, col + y
                explore_island(new_row, new_col)

        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1":
                    count += 1
                    explore_island(row, col)
        return count


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
    def numIslands(self, grid) -> int:

        # Number of rows
        m = len(grid)

        # Number of columns
        n = len(grid[0])

        # Instantiate a UFDS, representing each point in the matrix
        ufds = UFDS(m*n)

        # Keep track of number of points that are water
        count = 0
        for row in range(m):
            for col in range(n):

                # If this point is land
                if grid[row][col] == '1':

                    # We connect this land with the land directly below (if any)
                    if row + 1 < m and grid[row + 1][col] == '1':
                        ufds.union(row * n + col, (row + 1) * n + col)
                    # We connect this land with the land directly to the right (if any)
                    if col + 1 < n and grid[row][col + 1] == '1':
                        ufds.union(row * n + col, row * n + col + 1)
                else:
                    # Take note of number of rivers
                    count += 1

        # Count the total number of unique parents which will represent 'islands'
        unique = set()
        for i in range(m * n):
            # We relax all the points so that all connected points (ie islands) will have the same parent
            unique.add(ufds.find(i))

        # Subtract the number of water points in our UFDS
        return len(unique) - count

# grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# grid =[
# ["1","0","1","1","1"],
#  ["1","0","1","0","1"],
#  ["1","1","1","0","1"]
# ]
# print(Solution().numIslands(grid))