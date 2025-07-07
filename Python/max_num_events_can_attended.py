class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        days = max(end for start, end in events)
        count = 0
        heapify(events)
        available = []
        for day in range(days + 1):
            # Add valid events
            while events and day >= events[0][0]:
                start, end = heappop(events)
                heappush(available, end)
            # Remove events that are over
            while available and day > available[0]:
                heappop(available)
            if available:
                heappop(available)
                count += 1
        return count
