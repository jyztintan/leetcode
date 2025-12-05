class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def run(time):
            total = sum(min(time, batt) for batt in batteries)
            return total >= n * time

        low, high = 0, sum(batteries) // n
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if run(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
