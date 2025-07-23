class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def count(s, first, second, points):
            st = []
            total = 0
            for c in s:
                if st and st[-1] == first and c == second:
                    st.pop()
                    total += points
                else:
                    st.append(c)
            return total, "".join(st)

        ans = 0
        if x > y:
            pts, s = count(s, "a", "b", x)
            ans += pts
            pts, s = count(s, "b", "a", y)
            ans += pts
        else:
            pts, s = count(s, "b", "a", y)
            ans += pts
            pts, s = count(s, "a", "b", x)
            ans += pts
        return ans
