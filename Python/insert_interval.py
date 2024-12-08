class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        for idx, (start, end) in enumerate(intervals):
            if end < newInterval[0]:
                new_intervals.append([start, end])
            elif newInterval[1] < start:
                new_intervals.append(newInterval)
                return new_intervals + intervals[idx:]
            else:
                newInterval = [min(newInterval[0], start), max(newInterval[1], end)]

        new_intervals.append(newInterval)
        return new_intervals
