class MyCalendarTwo:

    def __init__(self):
        # Invariant: This should always be sorted
        self.bookings = []
        self.double = []

    def book(self, start: int, end: int) -> bool:

        def is_overlapping(start1, end1, start2, end2):
            return max(start1, start2) < min(end1, end2)

        def get_overlap(start1, end1, start2, end2):
            return [max(start1, start2), min(end1, end2)]

        for overlap_s, overlap_e in self.double:
            if is_overlapping(start, end, overlap_s, overlap_e):
                return False

        # Add new booking into self.bookings
        for s, e in self.bookings:
            # Update double bookings if overlap exists
            if is_overlapping(start, end, s, e):
                self.double.append(get_overlap(start, end, s, e))

        self.bookings.append([start, end])

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendarTwo()
# print(obj.book(10, 20))
# print(obj.book(15, 20))
# print(obj.book(20, 30))
# print(obj.book(17, 30))
