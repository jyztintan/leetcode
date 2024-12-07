class Solution:
    def solveNQueens(self, n: int):

        ans = []

        col = set()
        diag_up = set()
        diag_down = set()
        coordinates = set()
        def make_board(coordinates):
            board = [["."] * n for _ in range(n)]
            for x,y in coordinates:
                board[x][y] = "Q"
            for row in range(n):
                board[row] = "".join(board[row])
            return board

        def backtrack(queens):
            if queens == n:
                ans.append(make_board(coordinates))
                return

            for i in range(n):
                if i in col or i + queens in diag_up or i - queens in diag_down:
                    continue

                col.add(i)
                diag_up.add(i + queens)
                diag_down.add(i - queens)
                coordinates.add((queens, i))
                backtrack(queens + 1)
                col.remove(i)
                diag_up.remove(i + queens)
                diag_down.remove(i - queens)
                coordinates.remove((queens, i))

        backtrack(0)
        return ans