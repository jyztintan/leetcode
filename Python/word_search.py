class Solution:
    def exist(self, board, word: str) -> bool:
        if len(word) > len(board) * len(board[0]):
            return False
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            if col < 0 or row < 0 or row >= rows or col >= cols or board[row][col] != word[idx] or (row, col) in visited :
                return False

            visited.add((row, col))
            if dfs(row - 1, col, idx + 1) or dfs(row + 1, col, idx + 1) or dfs(row, col - 1, idx + 1) or dfs(row, col + 1, idx + 1):
                return True
            visited.remove((row, col))
            return False

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False

