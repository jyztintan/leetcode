import heapq

class Solution:
    def isNStraightHand(self, hand, groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        d = {}
        for num in hand:
            d[num] = d.get(num, 0) + 1

        min_heap = list(d.keys())
        heapq.heapify(min_heap)
        while min_heap:
            lowest = min_heap[0]
            for i in range(lowest, lowest + groupSize):
                if i not in d:
                    return False
                d[i] -= 1
                if d[i] == 0:
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True

hand = [1,2,3,6,2,3,4,7,8]
print(Solution().isNStraightHand(hand, 3))