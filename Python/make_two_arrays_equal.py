from typing import List

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        d = {}
        for num in target:
            d[num] = d.get(num, 0) + 1
        for num in arr:
            if num not in d:
                return False
            d[num] -= 1
        for num in d:
            if d[num] != 0:
                return False
        return True
