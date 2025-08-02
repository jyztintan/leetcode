class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        n = len(basket1)
        min_elem = float('inf')
        freq = defaultdict(int)
        for idx in range(n):
            num1, num2 = basket1[idx], basket2[idx]
            freq[num1] += 1
            freq[num2] -= 1
            min_elem = min(min_elem, num1, num2)

        leftover = []
        for num, count in freq.items():
            if count % 2:
                return -1
            leftover.extend([num] * (abs(count) // 2))

        if not leftover:
            return 0
        leftover.sort()
        total = 0

        # we only need to account for the lower half since cost = min(fruit1, fruit2)
        for num in leftover[:len(leftover) // 2]:
            # we can do indirect swap using the min_elem as an auxiliary element twice, if its cheaper
            total += min(2 * min_elem, num)
        return total
