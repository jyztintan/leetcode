class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        prev_shot = -float('inf')
        arrows = 0
        for start, end in points:
            if prev_shot < start:
                prev_shot = end
                arrows += 1
        return arrows
