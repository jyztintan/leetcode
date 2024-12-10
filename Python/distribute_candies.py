class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        # Set removes duplicate candies
        candy_types = len(set(candyType))

        n = len(candyType)
        num_eats = int(n / 2)
        return min(num_eats, candy_types)
