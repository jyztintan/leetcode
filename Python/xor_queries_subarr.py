from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        forward_xor = [0] * (n + 1)
        for i in range(1, n + 1):
            forward_xor[i] = forward_xor[i - 1] ^ arr[i - 1]
        ans = []
        for x, y in queries:
            ans.append(forward_xor[x] ^ forward_xor[y + 1])
        return ans

arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
print(Solution().xorQueries(arr, queries))
