class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(row, col, ptr):
            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            ori_char = board[row][col]
            if ori_char != word[ptr]:
                return False

            if ptr + 1 == len(word):
                return True

            board[row][col] = '#'
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                new_row, new_col = row + x, col + y
                if backtrack(new_row, new_col, ptr + 1):
                    return True
            board[row][col] = ori_char
            return False

        for row in range(m):
            for col in range(n):
                if backtrack(row, col, 0):
                    return True
        return False


