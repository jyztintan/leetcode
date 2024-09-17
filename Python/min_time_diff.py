class Solution:
    def findMinDifference(self, timePoints) -> int:
        timePoints.sort()

        # Help us find minute difference between 2 time points
        def find_diff(earlier, later):
            hours = int(later[:2]) - int(earlier[:2])
            minutes = int(later[-2:]) - int(earlier[-2:])
            total = hours * 60 + minutes
            mins_in_day = 60 * 24
            # Take the time taken from earliest -> later, or later -> earlier
            return min(mins_in_day - total, total)

        ans = float('inf')
        for i in range(len(timePoints) - 1):
            diff = find_diff(timePoints[i], timePoints[i + 1])
            ans = min(ans, diff)
        # Also account for the latest -> earliest
        ans = min(ans, find_diff(timePoints[0], timePoints[-1]))
        return ans
