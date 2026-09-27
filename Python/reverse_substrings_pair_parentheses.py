class Solution:
    def reverseParentheses(self, s: str) -> str:
        outer = []
        ans = []
        for c in s:
            if c == "(":
                outer.append(ans)
                ans = []
            elif c == ")":
                temp = ans
                ans = outer.pop()
                while temp:
                    ans.append(temp.pop())
            else:
                ans.append(c)
        return "".join(ans)

class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        curr = []

        for c in s:

            # If encounter an opening bracket, we add whatever we had in the stack for "storage"
            if c == "(":
                st.append(curr)
                curr = []

            # If encounter a closing bracket, we reverse the contents within the bracket
            # Then we continue the outer layer
            elif c == ")":
                curr = curr[::-1]
                curr = st.pop() + curr

            # Otherwise we keep building as per normal
            else:
                curr.append(c)

        return "".join(curr)

# print(Solution().reverseParentheses("(abcd)"))
# print(Solution().reverseParentheses("(u(love)i)"))
# print(Solution().reverseParentheses("(ed(et(oc))el)"))