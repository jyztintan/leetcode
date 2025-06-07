class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        min_heap = []
        for i, c in enumerate(s):
            if c == "*":
                small, j = heappop(min_heap)
                s[-j] = ""
                s[i] = ""
            else:
                heappush(min_heap, (c, -i))

        return "".join(s)
