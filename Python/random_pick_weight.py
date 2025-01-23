class Solution:

    def __init__(self, w: List[int]):
        self.n = len(w)
        self.prefix_sums = []
        curr = 0
        for num in w:
            curr += num
            self.prefix_sums.append(curr)
        self.total = curr

    def pickIndex(self) -> int:
        target = self.total * random.random()
        low, high = 0, self.n
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()