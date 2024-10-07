class Solution:
    def minLength(self, s: str) -> int:
        st = []
        for c in s:
            if not st:
                st.append(c)
                continue
            if (st[-1] == 'A' and c == 'B') or (st[-1] == 'C' and c == 'D'):
                st.pop()
                continue
            st.append(c)
        return len(st)