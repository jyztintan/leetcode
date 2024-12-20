# Time: O(N), Space: O(1) amazing elegant
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        max_ele = 0
        for idx, num in enumerate(arr):
            max_ele = max(max_ele, num)

            if max_ele == idx:
                count += 1
        return count

# Time: O(N), Space: O(N)
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0

        # Store indices that have not been matched to numbers
        missing = set()

        # Store numbers that have not been matched to indices
        extra = set()

        for idx, num in enumerate(arr):
            # Match index to stored number if applicable
            if idx not in extra:
                missing.add(idx)

            # Match num to stored index if applicable, otherwise store number
            if num in missing:
                missing.remove(num)
            else:
                extra.add(num)

            # If all matched, we can partition here
            if not missing:
                count += 1

        return count
