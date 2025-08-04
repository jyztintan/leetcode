class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        curr = {}
        best = 0
        for right, fruit in enumerate(fruits):
            if fruit not in curr:
                while len(curr) == 2:
                    left_fruit = fruits[left]
                    curr[left_fruit] -= 1
                    if curr[left_fruit] == 0:
                        del curr[left_fruit]
                    left += 1
            curr[fruit] = curr.get(fruit, 0) + 1
            best = max(best, right - left + 1)
        return best
