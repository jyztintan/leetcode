class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda i:i.start)
        busy = -float('inf')
        cannot = []
        for interval in intervals:
            if interval.start >= busy:
                busy = interval.end
            else:
                cannot.append(interval)
        return 1 + self.minMeetingRooms(cannot)

