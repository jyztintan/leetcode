class Solution:
    def smallestNumber(self, pattern: str) -> str:
        curr = 1
        ans = []
        st = []
        for c in pattern:
            if c == "I":
                ans.append(str(curr))
                while st:
                    ans.append(str(st.pop()))
            else:
                st.append(curr)
            curr += 1
        ans.append(str(curr))
        while st:
            ans.append(str(st.pop()))
        return "".join(ans)
