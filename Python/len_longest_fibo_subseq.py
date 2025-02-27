class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        arr_set = set(arr)
        best = 0
        n = len(arr)
        for first in range(n - 1):
            for second in range(first + 1, n):
                num1, num2 = arr[first], arr[second]
                nxt_val = num1 + num2
                curr = 2
                while nxt_val in arr_set:
                    num1, num2 = num2, nxt_val
                    nxt_val = num1 + num2
                    curr += 1
                    best = max(best, curr)
        return best
