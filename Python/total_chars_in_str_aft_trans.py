class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        for round in range(t):
            nxt = [0] * 26
            nxt[0] = count[25]
            nxt[1] = (count[25] + count[0]) % (10 ** 9 + 7)

            for i in range(2, 26):
                nxt[i] = count[i - 1]
            count = nxt

        return sum(count) % (10 ** 9 + 7)
