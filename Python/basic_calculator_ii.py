class Solution:
    def calculate(self, s: str) -> int:

        if not s:
            return 0

        s += "+"
        st = []
        curr = 0
        operation = "+"
        for c in s:
            if c.isdigit():
                curr = (curr * 10) + int(c)
            elif c != " ":
                if operation == "+":
                    st.append(curr)
                elif operation == "-":
                    st.append(-curr)
                elif operation == "*":
                    st.append(st.pop() * curr)
                elif operation == "/":
                    st.append(int(st.pop() / curr))
                operation = c
                curr = 0

        return sum(st)
