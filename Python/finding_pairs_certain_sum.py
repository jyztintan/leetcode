class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq1 = Counter(self.nums1)
        self.freq2 = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        self.freq2[num] -= 1
        self.nums2[index] += val
        self.freq2[num + val] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.freq1:
            count += self.freq1[num] * self.freq2[tot - num]
        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)