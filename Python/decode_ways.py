class Solution:
    def numDecodings(self, s: str) -> int:
        memoize = {len(s) : 1}

        def check(ptr):
            if ptr in memoize:
                return memoize[ptr]
            if s[ptr] == "0":
                memoize[ptr] = 0
                return memoize[ptr]

            total = check(ptr + 1)
            if (ptr + 2) <= len(s) and int(s[ptr:ptr+2]) <= 26:
                total += check(ptr + 2)
            memoize[ptr] = total
            return total

        check(0)
        return memoize[len(s)]