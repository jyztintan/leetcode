class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        gap = k
        for num in nums:
            if num == 0:
                gap += 1
            else:
                if gap < k:
                    return False
                gap = 0
        return True
