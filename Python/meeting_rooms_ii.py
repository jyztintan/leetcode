class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        d = {}
        for interval in intervals:
            d[interval[0]] = d.get(interval[0], 0) + 1
            d[interval[1]] = d.get(interval[1], 0) - 1

        concurrent = 0
        max_concurrent = 0

        for time in sorted(d.keys()):
            concurrent += d[time]
            max_concurrent = max(max_concurrent, concurrent)

        return max_concurrent


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i:i[0])
        busy = -float('inf')
        cannot = []
        for interval in intervals:
            if interval[0] >= busy:
                busy = interval[1]
            else:
                cannot.append(interval)
        return 1 + self.minMeetingRooms(cannot)
