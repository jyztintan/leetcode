class Solution:
    def countLargestGroup(self, n: int) -> int:
        largest_size = 0
        count_groups = 0
        sums = {}

        for num in range(1, n + 1):
            sum_digits = sum(map(int, str(num)))
            sums[sum_digits] = sums.get(sum_digits, 0) + 1
            if sums[sum_digits] > largest_size:
                largest_size = sums[sum_digits]
                count_groups = 1
            elif sums[sum_digits] == largest_size:
                count_groups += 1
        return count_groups
