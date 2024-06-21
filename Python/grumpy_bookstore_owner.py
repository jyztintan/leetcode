class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:

        # Total number of minutes
        n = len(customers)

        # Keep track of the already happy customers because owner was not grumpy
        happy_customers = 0

        # Keep track of unhappy customers turned away within a window of time
        unhappy_customers = 0

        # In the initial window starting from minute 0 to 'minutes'
        for i in range(minutes):
            if grumpy[i]:
                unhappy_customers += grumpy[i] * customers[i]
            else:
                happy_customers += customers[i]

        # We let the unhappy customers in the initial window be the starting base
        maximum_unhappy_customers = unhappy_customers

        # We slide this window period
        for i in range(minutes, n):

            # Decrement unhappy customers turned away outside the window
            unhappy_customers -= grumpy[i - minutes] * customers[i - minutes]

            # If in the new time period, owner is grumpy, then we keep track of that
            # Otherwise we add these to the already happy customers
            if grumpy[i]:
                unhappy_customers += grumpy[i] * customers[i]
            else:
                happy_customers += customers[i]

            # This allows us to keep track of when there is the most number of unhappy customers turned away
            # at any time window period
            maximum_unhappy_customers = max(maximum_unhappy_customers, unhappy_customers)

        # Add the already happy customers together with the maximum unhappy customers within a time period
        return maximum_unhappy_customers + happy_customers


# customers = [1,0,1,2,1,1,7,5]
# grumpy = [0,1,0,1,0,1,0,1]
# print(Solution().maxSatisfied(customers, grumpy, 3))