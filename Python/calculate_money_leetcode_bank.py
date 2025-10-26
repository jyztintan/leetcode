class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        curr = 1
        weekday = 0
        for day in range(n):
            total += curr
            curr += 1
            weekday += 1
            if weekday == 7:
                curr -= 6
                weekday = 0
        return total
