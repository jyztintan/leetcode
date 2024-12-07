class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # DFS 'escaped' regions from the border
        # All other grids in the middle WILL become captured
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col):
            if board[row][col] != "O":
                return
            board[row][col] = "E"
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if 0 <= new_row < m and 0 <= new_col < n:
                    dfs(new_row, new_col)

        for col in range(n):
            dfs(0, col)
            dfs(m - 1, col)

        for row in range(m):
            dfs(row, 0)
            dfs(row, n - 1)

        for row in range(m):
            for col in range(n):
                if board[row][col] == 'E':
                    board[row][col] = "O"
                else:
                    board[row][col] = "X"



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
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Number of rows
        m = len(board)

        # Number of columns
        n = len(board[0])

        # Instantiate a UFDS, representing each point in the matrix
        ufds = UFDS(m * n + 1)
        invalid = m * n

        for row in range(m):
            for col in range(n):

                # If this point is a region
                if board[row][col] == 'O':

                    # We connect this land with the land directly below (if any)
                    if row + 1 < m and board[row + 1][col] == 'O':
                        ufds.union(row * n + col, (row + 1) * n + col)
                    # We connect this land with the land directly to the right (if any)
                    if col + 1 < n and board[row][col + 1] == 'O':
                        ufds.union(row * n + col, row * n + col + 1)
                    if row == 0 or row == m - 1 or col == 0 or col == n - 1:
                        ufds.union(row * n + col, invalid)


        for row in range(m):
            for col in range(n):
                # If this point is a region
                if board[row][col] == 'O' and ufds.find(invalid) != ufds.find(row * n + col):
                    board[row][col] = 'X'

        return board

# board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# print(Solution().solve(board))