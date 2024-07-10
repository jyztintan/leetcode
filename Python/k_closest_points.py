import heapq
import math

# Solution 1: Simple Sort
class Solution:
    def kClosest(self, points, k: int):
        points.sort(key=lambda point:point[0] ** 2 + point[1] ** 2)
        return points[:k]


# Solution 2: Using Heap
class Solution:
    def kClosest(self, points, k: int):

        distances = []
        heapq.heapify(distances)

        for point in points:
            heapq.heappush(distances, (math.sqrt(point[0] ** 2 + point[1] ** 2), point))

        ans = []
        for i in range(k):
            dist, point = heapq.heappop(distances)
            ans.append(point)

        return ans


print(Solution().kClosest([[1,3],[0,0],[10,10]],2))