class Solution:
    def maxSatisfied(self, customers, grumpy, minutes: int) -> int:
        n = len(customers)

        happy_customers = 0
        unhappy_customers = 0
        for i in range(minutes):
            if grumpy[i]:
                unhappy_customers += grumpy[i] * customers[i]
            else:
                happy_customers += customers[i]

        maximum_unhappy_customers = unhappy_customers

        for i in range(minutes, n):
            unhappy_customers -= grumpy[i - minutes] * customers[i - minutes]
            if grumpy[i]:
                unhappy_customers += grumpy[i] * customers[i]
            else:
                happy_customers += customers[i]

            maximum_unhappy_customers = max(maximum_unhappy_customers, unhappy_customers)


        return maximum_unhappy_customers + happy_customers


customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
print(Solution().maxSatisfied(customers, grumpy, 3))