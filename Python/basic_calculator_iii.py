class Solution:
    def calculate(self, s: str) -> int:
        st = []
        processed = prev = curr = 0
        sign = "+"
        s += "+"
        for c in s:
            if c.isdigit():
                curr = curr * 10 + int(c)
            elif c == "(":
                st.append(processed)
                st.append(prev)
                st.append(sign)
                processed = prev = 0
                sign = "+"
            elif c in "+-*/)":
                if sign == "+":
                    processed += prev
                    prev = curr
                elif sign == "-":
                    processed += prev
                    prev = -curr
                elif sign == "*":
                    prev *= curr
                elif sign == "/":
                    prev = int(prev / curr)
                if c == ')':
                    curr = processed + prev
                    sign = st.pop()
                    prev = st.pop()
                    processed = st.pop()
                else:
                    sign = c
                    curr = 0
        return processed + prev
