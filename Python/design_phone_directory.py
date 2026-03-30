# Optimised because now the initialisation is also O(1)
class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = 0
        self.max = maxNumbers
        self.released = set()

    def get(self) -> int:
        if self.available == self.max and len(self.released) == 0:
            return -1
        if self.available < self.max:
            num = self.available
            self.available += 1
        else:
            num = self.released.pop()
        return num

    def check(self, number: int) -> bool:
        return number >= self.available or number in self.released

    def release(self, number: int) -> None:
        if number < self.available:
            self.released.add(number)


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.available = set(range(maxNumbers))

    def get(self) -> int:
        if not self.available:
            return -1
        num = self.available.pop()
        return num

    def check(self, number: int) -> bool:
        return number in self.available

    def release(self, number: int) -> None:
        self.available.add(number)

# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
