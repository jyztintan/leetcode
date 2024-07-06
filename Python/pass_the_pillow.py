class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % (2 * (n - 1))
        if time < n - 1:
            return time + 1
        else:
            time - n + 1
            return n - time - 1