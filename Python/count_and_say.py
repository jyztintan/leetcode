class Solution:
    def __init__(self):
        self.memoize = {}

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        if n in self.memoize:
            return self.memoize[n]

        prev = self.countAndSay(n - 1)
        prev += "$"  # end of str
        ptr = 0
        curr, count = prev[0], 0
        ans = ""
        for ptr in range(len(prev)):
            if prev[ptr] == curr:
                count += 1
            else:
                ans += str(count) + curr
                curr, count = prev[ptr], 1
        self.memoize[n] = ans
        return ans
