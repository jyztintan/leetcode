class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return "01" not in s # LOL

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        ptr = 0
        while ptr < len(s):
            if s[ptr] == '1':
                count += 1
                while ptr < len(s) and s[ptr] == '1':
                    ptr += 1
            ptr += 1
        return count <= 1