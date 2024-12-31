class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        undeleted = -float('inf')
        deleted = -float('inf')
        max_subarr = -float('inf')

        for num in arr:
            # undeleted: Continue undeleted or start new subarr
            # deleted: skip over this num (from undeleted) or continue adding after deletion
            undeleted, deleted = max(undeleted + num, num), max(undeleted, deleted + num)

            max_subarr = max(max_subarr, undeleted, deleted)

        return max_subarr
