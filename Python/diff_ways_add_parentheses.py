class Solution:
    def diffWaysToCompute(self, expression: str):

        def evaluate(expr: str):
            if len(expr) <= 2:
                return [int(expr)]

            res = []
            for i, c in enumerate(expr):
                if c.isdigit():
                    continue

                left_res = evaluate(expr[:i])
                right_res = evaluate(expr[i+1:])

                for left in left_res:
                    for right in right_res:
                        if c == '+':
                            res.append(left + right)
                        elif c == '-':
                            res.append(left - right)
                        elif c == '*':
                            res.append(left * right)

            return res

        return evaluate(expression)

# expression = "2-1-1"
# print(Solution().diffWaysToCompute(expression))
