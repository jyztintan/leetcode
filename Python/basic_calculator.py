class Solution:
    def calculate(self, s: str) -> int:

        # Store intermediate results as we process nested brackets
        st = []

        processed = 0
        curr = 0
        sign = 1

        for c in s:
            if c.isdigit():
                curr = (curr * 10) + int(c)
            elif c == "+":
                processed += curr * sign

                # Reset
                curr = 0
                sign = 1

            elif c == "-":
                processed += curr * sign

                # Reset
                curr = 0
                sign = -1

            elif c == "(":
                st.append(processed)
                st.append(sign)

                # Reset results
                processed = 0
                sign = 1

            elif c == ")":
                # Process the expression in the bracket
                processed += curr * sign
                # The sign before the brackets
                processed *= st.pop()
                # The value outside of the brackets
                processed += st.pop()

                curr = 0

        processed += curr * sign
        return processed
