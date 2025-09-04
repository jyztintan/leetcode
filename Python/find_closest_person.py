class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dist_x = abs(x - z)
        dist_y = abs(y - z)
        if dist_x < dist_y:
            return 1
        elif dist_y < dist_x:
            return 2
        return 0
