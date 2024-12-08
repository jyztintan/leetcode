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
