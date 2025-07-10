class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        largest_gap_forward = 0
        largest_gap_backward = 0
        prev1 = 0
        prev2 = eventTime
        can_fit = [False] * n
        for i in range(n):
            if endTime[i] - startTime[i] <= largest_gap_forward:
                can_fit[i] = True
            largest_gap_forward = max(largest_gap_forward, startTime[i] - prev1)
            prev1 = endTime[i]

            j = -i - 1
            if endTime[j] - startTime[j] <= largest_gap_backward:
                can_fit[j] = True
            largest_gap_backward = max(largest_gap_backward, prev2 - endTime[j])
            prev2 = startTime[j]

        best = 0
        for i in range(n):
            right = startTime[i + 1] if i != n - 1 else eventTime
            left = endTime[i - 1] if i != 0 else 0
            if can_fit[i]:
                best = max(best, right - left)
            else:
                best = max(best, right - left - (endTime[i] - startTime[i]))
        return best


