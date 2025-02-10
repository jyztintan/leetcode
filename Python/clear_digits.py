class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c.isnumeric() and st:
                st.pop()
            else:
                st.append(c)
        return "".join(st)
