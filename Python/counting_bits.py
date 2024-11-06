from math import *


class Solution:
    def countBits(self, n: int):
        ans = [0]
        if n == 0:
            return ans
        ans.append(1)
        for i in range(2, n + 1):
            ans.append(ans[i >> 1] + (i & 1))
        return ans

print(Solution().countBits(3))