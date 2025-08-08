class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        used = [False] * n
        count = 0
        for idx, fruit in enumerate(fruits):
            found = 1
            for ptr in range(n):
                if not used[ptr] and fruit <= baskets[ptr]:
                    used[ptr] = True
                    found = 0
                    break
            count += found
        return count
