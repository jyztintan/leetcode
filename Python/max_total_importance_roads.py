class Solution:
    def maximumImportance(self, n: int, roads) -> int:

        # Keep track of the number of cities each respective city is connected to
        lst = [0] * n
        for u, v in roads:
            lst[u] += 1
            lst[v] += 1

        # We sort the cities in increasing order of connectedness
        # The city number is irrelevant
        lst.sort()

        total = 0
        for i in range(1, n + 1):
            # Since our cities are already sorted, we greedily assign the most connected one with the highest importance
            total += i * lst[i - 1]

        return total


# roads = [[0,1]]
# print(Solution().maximumImportance(5, roads))