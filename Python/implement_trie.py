class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.child = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.child
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.child
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.child
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True