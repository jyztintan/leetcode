class Solution:
    def minGroups(self, intervals) -> int:
        d = {}
        for interval in intervals:
            d[interval[0]] = d.get(interval[0], 0) + 1
            d[interval[1] + 1] = d.get(interval[1] + 1, 0) - 1

        concurrent = 0
        max_concurrent = 0

        for time in sorted(d.keys()):
            concurrent += d[time]
            max_concurrent = max(max_concurrent, concurrent)

        return max_concurrent