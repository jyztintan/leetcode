class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        seen = set()
        for ele in nums:
            if ele in seen:
                seen.remove(ele)
            else:
                seen.add(ele)
        return len(seen) == 0
