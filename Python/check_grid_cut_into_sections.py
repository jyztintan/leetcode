class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        breadths = []
        heights = []
        for x1, y1, x2, y2 in rectangles:
            breadths.append([x1, x2])
            heights.append([y1, y2])

        def can_cut(intervals: List[List[int]]):
            intervals.sort()
            count, prev = 0, 0
            for ptr in range(len(intervals) - 1):
                prev = max(prev, intervals[ptr][1])
                if prev <= intervals[ptr + 1][0]:
                    count += 1
            return count >= 2

        return can_cut(breadths) or can_cut(heights)