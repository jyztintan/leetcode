class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        freq = defaultdict(int)
        for num in nums:
            freq[num % value] += 1
        for i in range(len(nums)):
            if freq[i % value] == 0:
                return i
            else:
                freq[i % value] -= 1
        return len(nums)
