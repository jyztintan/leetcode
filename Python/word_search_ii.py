class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Create Trie and insert words inside
        start = TrieNode()
        for word in words:
            curr = start
            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = word

        m, n = len(board), len(board[0])
        matched = []

        # Perform backtracking to find reachable words
        def backtrack(row, col, node):
            if row < 0 or row >= m or col < 0 or col >= n:
                return

            char = board[row][col]
            if char not in node.children:
                return

            next_node = node.children[char]
            if next_node.word:
                matched.append(next_node.word)
                next_node.word = None

            board[row][col] = '#'
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for x, y in directions:
                new_row, new_col = row + x, col + y
                backtrack(new_row, new_col, next_node)
            board[row][col] = char

        for row in range(m):
            for col in range(n):
                backtrack(row, col, start)
        return matched
