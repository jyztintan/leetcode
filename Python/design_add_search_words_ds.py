class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:

    def __init__(self):
        self.child = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.child
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.end = True

    def search(self, word: str) -> bool:
        return self.search_recursive(self.child, word)
    def search_recursive(self, node, word: str) -> bool:
        if not word:
            return node.end

        char = word[0]

        if char in node.children:
            return self.search_recursive(node.children[char], word[1:])

        if char == '.':
            for child in node.children:
                if self.search_recursive(node.children[child], word[1:]):
                    return True
        return False



# Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
word = "bad"
obj.addWord(word)
word = "..d"
print(obj.search(word))