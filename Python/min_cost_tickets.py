class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        buy_one_day, buy_week, buy_month = costs
        n = len(days)
        memo = {}

        def simulate(ptr):
            if ptr == n:
                return 0

            if ptr in memo:
                return memo[ptr]

            curr_day = days[ptr]

            # Simulate day pass
            one_day = buy_one_day + simulate(ptr + 1)

            # Just get the next time we need to buy the pass again
            next_ptr = ptr
            while next_ptr < n and days[next_ptr] < curr_day + 7:
                next_ptr += 1
            week = buy_week + simulate(next_ptr)

            while next_ptr < n and days[next_ptr] < curr_day + 30:
                next_ptr += 1
            month = buy_month + simulate(next_ptr)

            memo[ptr] = min(one_day, week, month)
            return memo[ptr]

        return simulate(0)
