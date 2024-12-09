class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        total_days = len(prices)
        day = 0
        # Get all the valleys and peaks as if k = infinity
        possible = []
        while day < total_days - 1:
            # While it is decreasing
            while day + 1 < total_days and prices[day] >= prices[day + 1]:
                day += 1
            valley = day
            # While it is increasing
            while day + 1 < total_days and prices[day] <= prices[day + 1]:
                day += 1
            peak = day
            possible.append([valley, peak])

        # We remove or merge the least profit transactions until we get only k transactions
        while len(possible) > k:

            # Find min loss for deleting a trxn
            delete_idx = 0
            min_delete_loss = float('inf')
            for i, (valley, peak) in enumerate(possible):
                profit_loss = prices[peak] - prices[valley]
                if profit_loss < min_delete_loss:
                    min_delete_loss = profit_loss
                    delete_idx = i

            # Find min loss for merging a trxn
            merge_idx = 0
            min_merge_loss = float('inf')
            for i in range(1, len(possible)):
                first_valley, first_peak = possible[i - 1]
                scnd_valley, scnd_peak = possible[i]
                profit_loss = prices[first_peak] - prices[scnd_valley]
                if profit_loss < min_merge_loss:
                    min_merge_loss = profit_loss
                    merge_idx = i

            if min_delete_loss <= min_merge_loss:
                possible.pop(delete_idx)
            else:
                possible[merge_idx - 1][1] = possible[merge_idx][1]
                possible.pop(merge_idx)

        profit = 0
        for valley, peak in possible:
            profit += prices[peak] - prices[valley]
        return profit
