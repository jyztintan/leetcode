class Solution:
    def sameEndSubstringCount(self, s: str, queries):
        n = len(s)
        prefix = [[] for _ in range(n)]
        cur = [0] * 26
        for i,c in enumerate(n):
            cur[ord(c) - ord('a')] += 1
            prefix[i] = cur.copy()
        res = []

        for start, end in queries:
            if start == 0:
                left = [0] * 26
            else:
                left = prefix[start - 1].copy()
            right = prefix[end].copy()
            cur_res = 0
            for x in range(26):
                right[x] = right[x] - left[x]
                cur_res = cur_res + right[x] * (right[x] + 1) // 2
            res.append(cur_res)

        return res