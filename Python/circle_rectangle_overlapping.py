class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x1 - radius <= xCenter <= x2 + radius and y1 <= yCenter <= y2:
            return True

        if x1 <= xCenter <= x2 and y1 - radius <= yCenter <= y2 + radius:
            return True

        def in_distance(x, y):
            return ((x - xCenter) ** 2 + (y - yCenter) ** 2) ** 0.5 <= radius

        return in_distance(x1, y1) or in_distance(x1, y2) or in_distance(x2, y1) or in_distance(x2, y2)
