class Solution:
    def partitionLabels(self, s: str):
        last = {c:i for i,c in enumerate(s)}
        start = end = 0
        ans = []
        for i,c in enumerate(s):
            # As we iterate through the characters, we extend the end if need be
            end = max(end,last[c])
            if i == end:
                ans.append(end - start + 1)
                start = end + 1

        return ans
