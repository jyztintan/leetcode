class Solution:
    def minDays(self, bloomDay, m: int, k: int) -> int:

        # This helps to ensure that it is even possible to get m bouquets of k adjacent flowers
        if m * k > len(bloomDay):
            return -1

        # This method helps us to find the number of bouquets we can make of k adjacent flowers
        # given an input number of days that have passed.
        def count_bouquets(days_passed):
            count = 0
            bouquets = 0
            for day in bloomDay:
                if day <= days_passed:
                    count += 1
                    if count == k:
                        bouquets += 1
                        count = 0
                else:
                    count = 0
            return bouquets

        # Must have at least one bloomed flower
        low = min(bloomDay)

        # Max is when all flowers have bloomed
        high = max(bloomDay)

        while low < high:
            mid = (low + high) // 2
            bouquets = count_bouquets(mid)

            # If the number of bouquets we have made is less than m, then we need to
            # increase the number of days passed so that more flowers have bloomed
            if bouquets < m:
                low = mid + 1

            # If the number of bouquets we make is equal to or exceeds m, then we can try to
            # decrease the number of days passed so as to optimise our solution
            if bouquets >= m:
                high = mid
        return low

# bloomDay = [1,10,2,9,3,8,4,7,5,6]
# print(Solution().minDays(bloomDay, 4, 2))
# bloomDay = [1,10,3,10,2]
# print(Solution().minDays(bloomDay, 3, 1))
# bloomDay = [1,10,3,10,2]
# print(Solution().minDays(bloomDay, 3, 2))
# bloomDay = [7,7,7,7,12,7,7]
# print(Solution().minDays(bloomDay, 2, 3))

