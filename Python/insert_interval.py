class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x:x[0])
        merged = []
        for start, end in intervals:
            if merged and merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        return self.merge(intervals)
