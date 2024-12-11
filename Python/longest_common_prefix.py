# Time: O(S * N) where S and N are the maximum str length and N is the number of strs
# Space: O(1)
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        first_word = strs[0]

        for i in range(len(first_word)):
            c = first_word[i]
            for word in strs[1:]:
                if i == len(word) or word[i] != c:
                    return first_word[:i]
        return strs[0]


# Time: O(S * N) where S and N are the maximum str length and N is the number of strs
# Space: O(S) because you store all possible prefixes
class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs:
            return ""

        first_word = strs[0]
        possible = set()
        for i in range(len(first_word)):
            possible.add(first_word[:i + 1])

        for word in strs[1:]:
            for prefix in possible.copy():
                if not word.startswith(prefix):
                    possible.remove(prefix)

        longest = ""
        for word in possible:
            if len(word) > len(longest):
                longest = word
        return longest
