class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        curr = 31
        while n:
            # isolate lowest bit and reverse it
            ans += (n & 1) << curr
            n >>= 1
            curr -= 1
        return ans
