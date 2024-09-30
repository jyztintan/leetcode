class CustomStack:

    def __init__(self, maxSize: int):
        self.st = [0] * maxSize
        self.size = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.size == self.maxSize:
            return
        self.st[self.size] = x
        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            return -1
        ans = self.st[self.size - 1]
        self.st[self.size - 1] = 0
        self.size -= 1
        return ans

    def increment(self, k: int, val: int) -> None:
        for i in range(min(k, self.size)):
            self.st[i] += val


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
obj.push(2)
obj.pop()
obj.push(2)
obj.push(3)
obj.push(4)
obj.increment(5, 100)
obj.increment(2, 100)
obj.pop()
