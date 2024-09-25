class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def __init__(self):
        self.root = Trie()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Trie()
            curr.children[c].count += 1
            curr = curr.children[c]

    def count(self, word):
        score = 0
        curr = self.root
        for c in word:
            score += curr.children[c].count
            curr = curr.children[c]
        return score

    def sumPrefixScores(self, words):
        ans = []
        for word in words:
            self.insert(word)
        for word in words:
            ans.append(self.count(word))
        return ans


print(Solution().sumPrefixScores(["abc", "ab", "bc", "b"]))
