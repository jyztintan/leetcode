# This only works because we are given that 0 <= from_i < to_i <= 1000
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events = [0] * 1001
        for passengers, start, end in trips:
            events[start] += passengers
            events[end] -= passengers

        curr = 0
        for i in range(1000):
            curr += events[i]
            if curr > capacity:
                return False
        return True


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])
        passengers = []
        curr = 0
        for board, start, end in trips:
            while passengers and start >= passengers[0][0]:
                _, alight = heappop(passengers)
                curr -= alight
            curr += board
            if curr > capacity:
                return False
            heappush(passengers, (end, board))
        return True
