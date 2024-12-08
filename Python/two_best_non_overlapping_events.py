# Min-Heap for start time to keep track of valid prev events
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:

        # Sorts events by their start time, in non-decreasing order
        events.sort()

        prev_event = 0
        best = 0
        pq = []

        for start, end, val in events:
            while pq and pq[0][0] < start:
                _, prev_val = heappop(pq)
                prev_event = max(prev_event, prev_val)

            best = max(best, prev_event + val)
            heappush(pq, (end, val))
        return best


# Brute Force TLE
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        best = 0
        for first_ptr in range(n):
            first_event = events[first_ptr]
            best = max(best, first_event[2])
            for second_ptr in range(first_ptr, n):
                second_event = events[second_ptr]
                if first_event[1] < second_event[0]:
                    best = max(best, first_event[2] + second_event[2])
        return best
