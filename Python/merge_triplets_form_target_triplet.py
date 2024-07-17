class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        max_a, max_b, max_c = 0, 0, 0
        for a, b, c in triplets:
            if a <= target[0] and b <= target[1] and c <= target[2]:
                max_a = max(max_a, a)
                max_b = max(max_b, b)
                max_c = max(max_c, c)
        return max_a == target[0] and max_b == target[1] and max_c == target[2]