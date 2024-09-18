from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort()
        slots2.sort()
        limit1 = len(slots1)
        limit2 = len(slots2)
        ptr1, ptr2 = 0, 0

        def find_overlap(slot1, slot2):
            start1, end1 = slot1
            start2, end2 = slot2
            total = max(end1, end2) - min(start1, start2)
            return end1 - start1 + end2 - start2 - total

        while ptr1 < limit1 and ptr2 < limit2:
            overlap = find_overlap(slots1[ptr1], slots2[ptr2])
            if overlap < duration:
                if slots1[ptr1][1] < slots2[ptr2][1]:
                    ptr1 += 1
                else:
                    ptr2 += 1
            else:
                start = max(slots1[ptr1][0], slots2[ptr2][0])
                return [start, start + duration]

slots1 = [[10,60]]
slots2 = [[12,17],[21,50]]
print(Solution().minAvailableDuration(slots1, slots2, 8))
