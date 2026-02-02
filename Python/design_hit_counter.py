class HitCounter:

    def __init__(self):
        self.timestamps = deque()

    def hit(self, timestamp: int) -> None:
        self.timestamps.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.timestamps and self.timestamps[0] <= timestamp - 300:
            self.timestamps.popleft()
        return len(self.timestamps)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
