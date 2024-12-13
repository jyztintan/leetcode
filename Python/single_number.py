class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = set()
        for num in nums:
            if num in seen_once:
                seen_once.remove(num)
            else:
                seen_once.add(num)
        return seen_once.pop()
