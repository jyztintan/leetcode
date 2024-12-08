class MyCalendarTwo:

    def __init__(self):
        self.bookings = []
        self.double_bookings = []

    def book(self, startTime: int, endTime: int) -> bool:
        for start, end in self.double_bookings:
            # Check for overlap
            if start < endTime and startTime < end:
                return False

        for start, end in self.bookings:
            # Check for overlap
            if start < endTime and startTime < end:
                # Get overlap
                overlap = [max(start, startTime), min(end, endTime)]
                self.double_bookings.append(overlap)

        self.bookings.append([startTime, endTime])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)