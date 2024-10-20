class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        st = []
        for i, c in enumerate(expression):
            if c == ')':
                val = []

                # Get all values within the parentheses
                while st[-1] != '(':
                    val.append(st.pop())

                st.pop()  # Ignore opening parentheses '('
                op = st.pop()
                resolved = self.process_substr(op, val)
                st.append(resolved)

            elif c != ',':
                st.append(c)

        return st[0] == 't'

    def process_substr(self, op, vals):
        if op == '&':
            return 't' if all(val == 't' for val in vals) else 'f'
        elif op == '|':
            return 't' if any(val == 't' for val in vals) else 'f'
        else:
            return 't' if vals[0] == 'f' else 'f'


# print(Solution().parseBoolExpr("!(&(f,t))"))
