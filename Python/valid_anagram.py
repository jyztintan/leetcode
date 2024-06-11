class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        for char in set(s):
            if s.count(char) != t.count(char):
                return False
        return True