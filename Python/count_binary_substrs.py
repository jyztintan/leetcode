class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count = 0
        prev_c, prev, curr = '', 0, 0
        for ptr in range(len(s)):
            if s[ptr] == prev_c:
                curr += 1
                continue
            count += min(prev, curr)
            prev_c = s[ptr]
            prev, curr = curr, 1
        return count + min(prev, curr)
