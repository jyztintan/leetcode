class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda x: x.start)
        busy = -float('inf')
        for interval in intervals:
            if interval.start < busy:
                return False
            busy = interval.end
        return True
