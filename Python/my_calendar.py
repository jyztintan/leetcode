class MyCalendar:

    def __init__(self):
        # Invariant: This should always be sorted
        self.booked = [[0, 0]]

    def book(self, start: int, end: int) -> bool:
        new = []
        added = False
        for s, e in self.booked:
            if e <= start:
                new.append([s, e])
            elif s >= end:
                if not added:
                    new.append([start, end])
                    added = True
                new.append([s, e])
            else:
                return False

        if not added:
            new.append([start, end])

        self.booked = new
        return True

# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10,20))
print(obj.book(15,20))
print(obj.book(20,30))
