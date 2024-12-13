class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_occur = {}
        for idx, c in enumerate(nums):
            if c in num_occur and num_occur[c] + k >= idx:
                return True
            num_occur[c] = idx
        return False
