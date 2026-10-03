class Solution:
    def longestValidParentheses(self, s: str) -> int:
        match = 0
        n = len(s)
        open, close = 0, 0
        for i in range(n):
            c = s[i]
            if c == "(":
                open += 1
            else:
                close += 1
                if close > open:
                    open, close = 0, 0
            if open == close:
                match = max(match, close)

        open, close = 0, 0
        for i in range(n):
            c = s[- i - 1]
            if c == ")":
                close += 1
            else:
                open += 1
                if open > close:
                    open, close = 0, 0
            if open == close:
                match = max(match, close)

        return match * 2
