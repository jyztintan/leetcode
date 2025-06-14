class Solution:
    def minMaxDifference(self, num: int) -> int:
        max_val = 0
        min_val = float('inf')
        for i in range(10):
            i = str(i)
            max_val = max(max_val, int(str(num).replace(i, "9")))
            min_val = min(min_val, int(str(num).replace(i, "0")))
        return max_val - min_val
