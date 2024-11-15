import heapq


class Solution:
    def shareCandies(self, candies, k: int) -> int:
        total = {}
        for candy in candies[k:]:
            total[candy] = total.get(candy, 0) + 1

        best = len(total)
        for i in range(len(candies) - k):
            add_candy = candies[i]
            total[add_candy] = total.get(add_candy, 0) + 1

            remove_candy = candies[i + k]
            total[remove_candy] -= 1
            if total[remove_candy] == 0:
                del total[remove_candy]

            best = max(best, len(total))

        return best
