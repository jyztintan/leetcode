class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        lucky = -1
        for num in freq:
            if freq[num] == num:
                lucky = max(lucky, num)
        return lucky
