from heapq import *
from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        max_incr_heap = []
        for passes, total in classes:
            heappush(max_incr_heap, (-((passes + 1) / (total + 1) - (passes / total)), passes, total))

        for _ in range(extraStudents):
            _, passes, total = heappop(max_incr_heap)
            new_passes, new_total = passes + 1, total + 1
            heappush(max_incr_heap, (- ((new_passes + 1) / (new_total + 1) - (new_passes / new_total)), new_passes, new_total))

        pass_ratio = 0
        for ratio, passes, total in max_incr_heap:
            pass_ratio += passes/total
        return pass_ratio / len(classes)


classes = [[2,4],[3,9],[4,5],[2,10]]
print(Solution().maxAverageRatio(classes, 2))