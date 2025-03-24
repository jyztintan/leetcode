# Time: O(NlogN), where N is the number of meetings
# Space: O(N)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        meetings.append([days + 1, days + 1])

        no_meetings = meetings[0][0] - 1
        prev_end = 0
        for idx in range(len(meetings) - 1):
            start, end = meetings[idx]
            prev_end = max(prev_end, end)
            next_start, next_end = meetings[idx + 1]
            if prev_end >= next_start:
                continue
            no_meetings += next_start - prev_end - 1
        return no_meetings

# MLE: Space complexity of O(days)
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        total_meetings = [0] * (days + 1)
        for start, end in meetings:
            total_meetings[start - 1] += 1
            total_meetings[end] -= 1

        no_meetings = 0
        curr = 0
        for day in range(days):
            curr += total_meetings[day]
            if curr == 0:
                no_meetings += 1
        return no_meetings
