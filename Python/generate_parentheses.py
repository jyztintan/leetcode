class Solution:
    def generateParenthesis(self, n):
    
        res = []
        string = ""

        def generate_answer(string, open, close):
            if open == close == n:
                res.append(string)

            if open < n:
                generate_answer(string + '(', open + 1, close)

            if close < open:
                generate_answer(string + ')', open, close + 1)

        generate_answer(string, 0,0)
        return res

# sol = Solution()
# print(sol.generateParenthesis(3))
# print(generate_parenthesis(1))
# print(generate_parenthesis(2))
# print(generate_parenthesis(3))
# print(generate_parenthesis(4))
