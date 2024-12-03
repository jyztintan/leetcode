class Solution:
    def addSpaces(self, s: str, spaces) -> str:
        ptr = 0
        spaces = set(spaces)
        ans = ""
        for i, c in enumerate(s):
            if i in spaces:
                ptr += 1
                ans += " "
            ans += c
        return ans
