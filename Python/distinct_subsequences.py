# O(M x N) time and space complexity because of memoization and possible recursive calls
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def count(ptr_s, ptr_t):
            # Target reached
            if ptr_t == len(t):
                return 1
            # No more characters to continue
            if ptr_s == len(s):
                return 0

            # Calculated before
            if (ptr_s, ptr_t) in memo:
                return memo[(ptr_s, ptr_t)]

            # Different char so move s_ptr forward
            if s[ptr_s] != t[ptr_t]:
                memo[(ptr_s, ptr_t)] = count(ptr_s + 1, ptr_t)
            else:
                # Same char so we either use or dont use the char in s_ptr
                memo[(ptr_s, ptr_t)] = count(ptr_s + 1, ptr_t) + count(ptr_s + 1, ptr_t + 1)
            return memo[(ptr_s, ptr_t)]

        return count(0, 0)
