class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        target = len(part)
        part = list(part)
        st = []

        for c in s:
            st.append(c)
            if st[-target:] == part:
                st = st[:-target]

        return "".join(st)
