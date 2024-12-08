class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        remove_start, remove_end = toBeRemoved
        new_intervals = []
        for start, end in intervals:
            if start < remove_end and remove_start < end:
                if start < remove_start:
                    new_intervals.append([start, remove_start])
                if end > remove_end:
                    new_intervals.append([remove_end, end])
            else:
                new_intervals.append([start, end])
        return new_intervals
