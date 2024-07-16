import queue
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        m = len(beginWord)
        substring_map = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(m):
                substring = word[:i] + "*" + word[i+1:]
                substring_map[substring].append(word)
        visited = set()
        visited.add(beginWord)
        q = queue.Queue()
        q.put(beginWord)
        ans = 1
        while not q.empty():
            for i in range(q.qsize()):
                word = q.get()
                if word == endWord:
                    return ans
                for i in range(m):
                    substring = word[:i] + "*" + word[i + 1:]
                    for neighbour in substring_map[substring]:
                        if neighbour not in visited:
                            q.put(neighbour)
                            visited.add(neighbour)
            ans += 1
        return 0

wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength("hit", "cog", wordList))