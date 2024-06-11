class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st = []
        for token in tokens:

            # note that isdigit() returns false for negative numbers
            if token[-1].isdigit():
                st.append(int(token))
                continue
            second = st.pop()
            first = st.pop()
            if token == "+":
                st.append(first + second)
            elif token == "-":
                st.append(first - second)
            elif token == "*":
                st.append(first * second)
            else:
                st.append(int(first/second))
        return st[0]


# sol = Solution()
# # tokens = ["2","1","+","3","*"]
# # print(sol.evalRPN(tokens))
# # tokens = ["4","13","5","/","+"]
# # print(sol.evalRPN(tokens))
# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# print(sol.evalRPN(tokens))
# tokens =["4","-2","/","2","-3","-","-"]
# print(sol.evalRPN(tokens))
