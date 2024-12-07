class Solution:
    def totalNQueens(self, n: int) -> int:

        count = [0]
        col = set()
        diag_up = set()
        diag_down = set()
        coordinates = set()

        def backtrack(queens):
            if queens == n:
                count[0] += 1
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
        return count[0]