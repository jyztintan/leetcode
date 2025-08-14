class Solution:
    def largestGoodInteger(self, num: str) -> str:
        st = []
        best = ""
        for c in num:
            if st and c == st[-1]:
                if len(st) == 2:
                    best = max(best, c)
                else:
                    st.append(c)
            else:
                st = [c]
        return best * 3
