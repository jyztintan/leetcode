class Solution:
    def maxOperations(self, s: str) -> int:
        ones = 0
        n = len(s)
        ptr = 0
        count = 0
        while ptr < n:
            if s[ptr] == '0':
                while ptr < n and s[ptr] == '0':
                    ptr += 1
                count += ones
            else:
                ones += 1
                ptr += 1
        return count
