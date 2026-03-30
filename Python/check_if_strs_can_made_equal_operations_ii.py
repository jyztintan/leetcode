class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        odd = {}
        even = {}
        for i, c in enumerate(s1):
            if i % 2:
                odd[c] = odd.get(c, 0) + 1
            else:
                even[c] = even.get(c, 0) + 1
        for i, c in enumerate(s2):
            if i % 2:
                if odd.get(c, 0) == 0:
                    return False
                odd[c] -= 1
            else:
                if even.get(c, 0) == 0:
                    return False
                even[c] -= 1
        return True
