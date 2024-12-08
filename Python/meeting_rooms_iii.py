from heapq import *


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        count = [0] * n

        # Keep track of next available timing for a used room
        used = []
        unused = list(range(n))
        heapify(unused)
        meetings.sort()

        for start, end in meetings:
            while used and used[0][0] <= start:
                _, room = heappop(used)
                heappush(unused, room)

            if unused:
                room = heappop(unused)
                heappush(used, [end, room])

            else:
                curr_end, room = heappop(used)
                heappush(used, [curr_end + end - start, room])

            count[room] += 1

        return count.index(max(count))
