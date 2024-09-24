# Solution 1: Prefix HashSet
class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        possible = set()
        for num in arr1:
            for i in range(len(num)):
                possible.add(num[:i + 1])
        longest = 0
        for num in arr2:
            for i in range(len(num)):
                if num[:i + 1] in possible:
                    longest = max(longest, i + 1)
        return longest

# Solution 2: Trie
class Solution:
    def longestCommonPrefix(self, arr1, arr2) -> int:
        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))
        trie = {}
        for num in arr1:
            traverse = trie
            for c in num:
                if c not in traverse:
                    traverse[c] = {}
                traverse = traverse[c]

        longest = 0
        for num in arr2:
            traverse = trie
            depth = 0
            for c in num:
                if c not in traverse:
                    break
                traverse = traverse[c]
                depth += 1
            longest = max(longest, depth)
        return longest


print(Solution().longestCommonPrefix([1, 10,100], [1000]))
