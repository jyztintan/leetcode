class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda x: x[0])
        busy = -float('inf')
        for interval in intervals:
            if interval.start < busy:
                return False
            busy = interval.end
        return True
