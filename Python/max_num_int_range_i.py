class Solution:
    def maxCount(self, banned, n: int, maxSum: int) -> int:
        banned = set(banned)
        curr_sum = 0
        count = 0
        for num in range(1, n + 1):
            if num in banned:
                continue
            if curr_sum + num > maxSum:
                break
            curr_sum += num
            count += 1
        return count
