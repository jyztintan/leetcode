class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        prefix_sum = [0]
        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + endTime[i] - startTime[i])

        best = 0
        for l in range(n - k + 1):
            # if its the first one then start at 0
            # otherwise take the end time of the prev event
            left = 0 if l == 0 else endTime[l - 1]
            # if its the last one then right bound is eventTime
            # otherwise take the start time of the next event
            right = eventTime if l == n - k else startTime[l + k]
            # the free time is the time in the window: right - left
            # and removing the time spent on meetings
            best = max(best, right - left - prefix_sum[l + k] + prefix_sum[l])
        return best
