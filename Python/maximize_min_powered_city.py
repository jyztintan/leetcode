class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        count = [0] * (n + 1)

        # create a sweep line
        for i in range(n):
            left = max(0, i - r)
            right = min(n, i + r + 1)
            count[left] += stations[i]
            count[right] -= stations[i]

        def check(limit):
            sweep = count[::]
            curr = 0
            chances = k

            for i in range(n):
                curr += sweep[i]
                if curr < limit:
                    deficit = limit - curr
                    if chances < deficit:
                        return False
                    curr += deficit
                    chances -= deficit
                    new_station = min(n, i + 2 * r + 1)
                    sweep[new_station] -= deficit

            return True

        low, high = min(stations), sum(stations) + k
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans


