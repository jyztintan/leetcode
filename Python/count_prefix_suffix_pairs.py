class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for right, word in enumerate(words):
            for left in range(right):
                sub = words[left]
                if self.isPrefixAndSuffix(sub, word):
                    count += 1
        return count

    def isPrefixAndSuffix(self, w1, w2):
        return w2.startswith(w1) and w2.endswith(w1)
