class Solution:
    def numTeams(self, rating) -> int:
        n = len(rating)

        two_seq_increasing = [0] * n
        full_seq_increasing = [0] * n
        two_seq_decreasing = [0] * n
        full_seq_decreasing = [0] * n

        for left in range(n - 1, -1, -1):
            count_two_seq_increasing = 0
            count_full_seq_increasing = 0
            count_two_seq_decreasing = 0
            count_full_seq_decreasing = 0
            for right in range(left + 1, n):
                if rating[left] < rating[right]:
                    count_two_seq_increasing += 1
                    count_full_seq_increasing += two_seq_increasing[right]
                if rating[left] > rating[right]:
                    count_two_seq_decreasing += 1
                    count_full_seq_decreasing += two_seq_decreasing[right]
            two_seq_increasing[left] = count_two_seq_increasing
            full_seq_increasing[left] = count_full_seq_increasing
            two_seq_decreasing[left] = count_two_seq_decreasing
            full_seq_decreasing[left] = count_full_seq_decreasing

        return sum(full_seq_increasing) + sum(full_seq_decreasing)

