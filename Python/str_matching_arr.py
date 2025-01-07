# O(N^2 * M)
# Just concatenate all and find the words that occur more than once
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        everything = '#'.join(words)
        matching = []
        for word in words:
            if everything.count(word) > 1:
                matching.append(word)
        return matching

# O(N x M ^ 2)
class TrieNode:
    def __init__(self):
        self.children = {}
        self.frequency = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.frequency += 1

    def is_substring(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
        return curr.frequency > 1


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        matching = []
        trie = Trie()

        for word in words:
            # A substring can also be the later part of the string
            for start_idx in range(len(word)):
                trie.insert_word(word[start_idx])

        for word in words:
            if trie.is_substring(word):
                matching.append(word)

        return matching
