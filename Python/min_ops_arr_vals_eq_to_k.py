class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        greater = set()
        for num in nums:
            if num < k:
                return -1
            if num != k:
                greater.add(num)

        return len(greater)
