class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        dictionary = defaultdict(list)
        for word in wordList:
            for i in range(n):
                intermediate_word = word[:i] + '*' + word[i + 1:]
                dictionary[intermediate_word].append(word)

        q = deque()
        q.append((beginWord, 1))
        visited = set([beginWord])
        while q:
            word, count = q.popleft()
            if word == endWord:
                return count

            for i in range(n):
                intermediate_word = word[:i] + '*' + word[i + 1:]
                for next_word in dictionary[intermediate_word]:
                    if next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, count + 1))
                dictionary[intermediate_word] = []
        return 0