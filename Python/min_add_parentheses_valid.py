class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count = 0
        ans = 0
        # loop through
        for c in s:
            if c == "(":
                count += 1
            else:
                if count == 0:
                    ans += 1
                count = max(0, count - 1)

        # cover remaining opens
        ans += count
        return ans



