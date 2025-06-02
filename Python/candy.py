class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        ascending = [0] * n
        for idx in range(1, n):
            if ratings[idx] > ratings[idx - 1]:
                ascending[idx] = ascending[idx - 1] + 1

        descending = [0] * n
        for idx in range(n - 2, -1, -1):
            if ratings[idx] > ratings[idx + 1]:
                descending[idx] = descending[idx + 1] + 1

        count = n
        for idx in range(n):
            count += max(ascending[idx], descending[idx])
        return count


