# Optimised O(N) time complexity: 2 passes
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        freq = {}
        for ptr in range(len(s)):
            freq[s[ptr]] = freq.get(s[ptr], 0) + 1
            freq[t[ptr]] = freq.get(t[ptr], 0) - 1
        for c in freq:
            if freq[c] != 0:
                return False
        return True


# L this is O(N^2) time complexity
class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True
