class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self, n):
        self.head = TrieNode()
        self.n = n

    def insert_word(self, word):
        curr = self.head
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

    def find(self, word, ptr, curr, chance):
        if ptr == self.n:
            return True

        c = word[ptr]
        if c in curr.children:
            if self.find(word, ptr + 1, curr.children[c], chance):
                return True

        if chance > 0:
            for possible in curr.children:
                if self.find(word, ptr + 1, curr.children[possible], chance - 1):
                    return True
        return False


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        trie = Trie(n)
        for word in dictionary:
            trie.insert_word(word)

        ans = []
        for q in queries:
            if trie.find(q, 0, trie.head, 2):
                ans.append(q)

        return ans
