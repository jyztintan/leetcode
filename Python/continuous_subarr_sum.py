class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_mod = 0
        seen_mod = {0: -1}

        for idx, num in enumerate(nums):
            prefix_mod = (prefix_mod + num) % k

            if prefix_mod in seen_mod:
                if idx - seen_mod[prefix_mod] >= 2:
                    return True
            else:
                seen_mod[prefix_mod] = idx

        return False