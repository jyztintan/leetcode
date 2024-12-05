class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        brackets = []

        def dfs(open, close):
            if len(brackets) == n * 2:
                res.append("".join(brackets))

            if open > 0:
                brackets.append("(")
                dfs(open - 1, close)
                brackets.pop()

            if close > open:
                brackets.append(")")
                dfs(open, close - 1)
                brackets.pop()

        dfs(n, n)
        return res

# sol = Solution()
# print(sol.generateParenthesis(3))
# print(generate_parenthesis(1))
# print(generate_parenthesis(2))
# print(generate_parenthesis(3))
# print(generate_parenthesis(4))
