class Solution:
    def averageWaitingTime(self, customers) -> float:

        # Keeps track of total waiting time
        wait = 0

        # Keeps track of current chef's business
        chef = 1

        for arrival, time in customers:

            # For every customer there are 2 scenarios
            # 1) The chef was already available so when this customer comes in, he will cook immediately upon arrival
            # 2) The chef was already busy, so we just add on the new customer's order onto the chef's schedule
            if arrival >= chef:
                chef = arrival + time
            else:
                chef += time

            # The chef's status is now updated to when this customer's meal will be ready
            # Hence, we just need to sum the difference between this and their respective arrival time
            wait += chef - arrival

        return wait / len(customers)

# customers = [[1,2],[2,5],[4,3]]
# print(Solution().averageWaitingTime(customers))
# customers = [[5,2],[5,4],[10,3],[20,1]]
# print(Solution().averageWaitingTime(customers))
