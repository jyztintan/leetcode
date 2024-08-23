import math


class Solution:
    def fractionAddition(self, expression: str) -> str:
        ptr = 0
        numerator = 0
        denominator = 1
        if expression[ptr] != "-":
            expression = "+" + expression
        while ptr < len(expression):

            add = 1 if expression[ptr] == "+" else -1
            ptr += 1

            # Get current numerator
            num_start = ptr
            while expression[ptr].isdigit():
                ptr += 1
            curr_numerator = int(expression[num_start:ptr])

            # Skip "/"
            ptr += 1

            # Get current denominator
            denom_start = ptr
            while ptr < len(expression) and expression[ptr].isdigit():
                ptr += 1
            curr_denominator = int(expression[denom_start:ptr])

            numerator = numerator * curr_denominator + add * curr_numerator * denominator
            denominator = denominator * curr_denominator

        gcd = math.gcd(numerator, denominator)
        numerator //= gcd
        denominator //= gcd
        return str(numerator) + "/" + str(denominator)

# print(Solution().fractionAddition("-5/2+10/3+7/9"))
# print(Solution().fractionAddition("-1/2+1/2+1/3"))
# print(Solution().fractionAddition("1/3-1/2"))

