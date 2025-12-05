from collections import defaultdict
from math import *

class Solution:
    def countTrapezoids(self, points) -> int:
        points = list(set((x, y) for x, y in points))
        gradient = defaultdict(int)
        for i, (x1, y1) in enumerate(points):
            for x2, y2 in points[i + 1:]:
                if x2 == x1:
                    m = float('inf')
                else:
                    m = (y2 - y1)/(x2 - x1)
                gradient[m] += 1

        print(gradient)
        ans = 0
        for count in gradient.values():
            ans += comb(count, 2)
        return ans


points = [[-32,12],[-32,-94],[-32,-15],[-30,88]]
print(Solution().countTrapezoids(points))