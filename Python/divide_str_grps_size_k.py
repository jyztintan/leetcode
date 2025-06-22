class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        ans = []
        for i in range(len(s) // k + 1):
            ans.append(s[i * k: (i + 1) * k])
        if ans[-1] == "":
            ans.pop()
        else:
            ans[-1] = ans[-1] +  (k - len(ans[-1])) * fill
        return ans
