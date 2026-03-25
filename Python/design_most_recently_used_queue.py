class MRUQueue:

    def __init__(self, n: int):
        self.st = list(range(1, n + 1))

    def fetch(self, k: int) -> int:
        num = self.st.pop(k - 1)
        self.st.append(num)
        return num

# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)
