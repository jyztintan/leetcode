from typing import List

# Functional Programming
# Time Complexity: O(nlogn + m*n), where n = len(products), m = len(searchWord)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        ans = []
        for i in range(1, len(searchWord) + 1):
            products = list(filter(lambda s:s.startswith(searchWord[:i]), products))
            ans.append(products[:3])
        return ans


# Trie
# Time Complexity: O(m), where m = len(searchWord)
class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.end = False


class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.res = []

    def insert(self, word: str) -> None:
        current = self.root
        for letter in word:
            index = ord(letter) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.end = True

    def dfs_prefix(self, node, prefix: str) -> bool:
        if len(self.res) == 3:
            return

        if node.end:
            self.res.append(prefix)

        for i in range(26):
            if node.children[i]:
                self.dfs_prefix(node.children[i], prefix + chr(i + ord('a')))

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        self.res = []
        for c in prefix:
            index = ord(c) - ord('a')
            if not curr.children[index]:
                return self.res
            curr = curr.children[index]
        self.dfs_prefix(curr, prefix)
        return self.res


    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        for product in products:
            self.insert(product)
        res = []
        prefix = ''
        for c in searchWord:
            prefix += c
            res.append(self.startsWith(prefix))
        return res