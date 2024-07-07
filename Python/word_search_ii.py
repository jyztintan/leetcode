class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

class Solution:

    def findWords(self, board, words):
        root = TrieNode()
        rows, cols = len(board), len(board[0])
        ans, visited = set(), set()

        for word in words:
            root.add_word(word)

        def dfs(row, col, node, word):
            if col < 0 or row < 0 or row >= rows or col >= cols or board[row][col] not in node.children or (row, col) in visited :
                return

            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]
            if node.end:
                node.end = False
                ans.add(word)

            dfs(row - 1, col, node, word)
            dfs(row + 1, col, node, word)
            dfs(row, col - 1, node, word)
            dfs(row, col + 1, node, word)
            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] not in root.children:
                    continue
                dfs(row, col, root, "")

        return list(ans)