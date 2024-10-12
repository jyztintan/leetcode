import heapq


class Solution:
    def smallestChair(self, times, targetFriend: int) -> int:
        events = sorted((time[0], time[1], i) for i, time in enumerate(times))

        chairs = list(range(len(times)))
        heapq.heapify(chairs)
        occupied = []

        for start, end, friend in events:
            while occupied and occupied[0][0] <= start:
                _, chair = heapq.heappop(occupied)
                heapq.heappush(chairs, chair)

            best = heapq.heappop(chairs)

            if friend == targetFriend:
                return best
            heapq.heappush(occupied, (end, best))


times = [[33889,98676],[80071,89737],[44118,52565],[52992,84310],[78492,88209],[21695,67063],[84622,95452],[98048,98856],[98411,99433],[55333,56548],[65375,88566],[55011,62821],[48548,48656],[87396,94825],[55273,81868],[75629,91467]]
print(Solution().smallestChair(times, 6))







