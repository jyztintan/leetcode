class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort(reverse=True)

        # Count the maximum number of non-overlapping tasks
        count = 0
        start = float('inf')
        for interval in intervals:
            if interval[1] <= start:
                start = interval[0]
                count += 1

        # We just need to remove the difference between the total intervals and the max number of non-overlapping tasks.
        return len(intervals) - count
