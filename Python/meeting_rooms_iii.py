from heapq import *

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n

        available = list(range(n))  # sort by room
        heapify(available)
        used = []  # sort by end time

        for start, end in sorted(meetings):
            # vacate rooms that have ended their meetings
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(available, room)

            if available:  # use available if any
                room = heappop(available)
                heappush(used, (end, room))
            else:  # otherwise delay to next available
                duration = end - start
                time, room = heappop(used)
                heappush(used, (time + duration, room))

            count[room] += 1

        return count.index(max(count))
