class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = ""
        # Prev char and count
        prev = ['', 0]
        for c in s:
            if c == prev[0] and prev[1] < 2:
                ans += c
                prev[1] += 1
            elif c != prev[0]:
                prev = [c, 1]
                ans += c
        return ans
