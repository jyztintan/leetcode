class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n != len(s2):
            return False

        replace = []
        for ptr in range(n):
            if s1[ptr] != s2[ptr]:
                if len(replace) == 2:
                    return False
                else:
                    replace.append(ptr)

        return len(replace) == 0 or (
                    len(replace) == 2 and s1[replace[0]] == s2[replace[1]] and s1[replace[1]] == s2[replace[0]])
