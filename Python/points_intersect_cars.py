# O(N) Line Sweep - since carpark only has 100 lots
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        carpark = [0] * 102
        for start, end in nums:
            carpark[start] += 1
            carpark[end + 1] -= 1

        count = 0
        cars = 0
        for lot in range(101):
            cars += carpark[lot]
            if cars:
                count += 1
        return count


# O(NlogN) Merge Intervals strategy
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        intervals = []
        for start, end in nums:
            if intervals and start <= intervals[-1][1]:
                intervals[-1][1] = max(intervals[-1][1], end)
            else:
                intervals.append([start, end])

        count = 0
        for start, end in intervals:
            count += end - start + 1
        return count


