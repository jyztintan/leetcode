class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        board = [[0 for _ in range(n)] for _ in range(m)]
        for row in range(m):
            for col in range(n):
                # If it is a corner tile, then there is only one way to get there
                if row == 0 or col == 0:
                    board[row][col] = 1
                else:
                    # Otherwise the number of ways to get to this tile is either by moving down from the tile above
                    # Or moving right from the tile to the left
                    # So, total number of ways to curr tile = #ways to tile above + #ways to left adjacent tile
                    board[row][col] = board[row - 1][col] + board[row][col - 1]
        return board[-1][-1]

# print(Solution().uniquePaths(2, 2))