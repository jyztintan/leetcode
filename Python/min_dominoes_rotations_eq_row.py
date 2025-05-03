# Also O(N) time but we don't need to find the majority element - just kind of trial and error twice
# This is an improvement with O(1) space
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        swap_top, swap_bottom = 0, 0
        target_top = tops[0]
        for i in range(n):
            if tops[i] != target_top and bottoms[i] != target_top:
                swap_top, swap_bottom = -1, -1
                break
            if bottoms[i] == target_top and tops[i] != target_top:
                swap_top += 1
            elif tops[i] == target_top and bottoms[i] != target_top:
                swap_bottom += 1

        if swap_top != -1:
            return min(swap_top, swap_bottom)

        swap_top, swap_bottom = 0, 0
        target_bottom = bottoms[0]
        for i in range(n):
            if tops[i] != target_bottom and bottoms[i] != target_bottom:
                swap_top, swap_bottom = -1, -1
                break
            if bottoms[i] == target_bottom and tops[i] != target_bottom:
                swap_top += 1
            elif tops[i] == target_bottom and bottoms[i] != target_bottom:
                swap_bottom += 1

        if swap_top != -1:
            return min(swap_top, swap_bottom)
        return -1


# O(N) time - 1) find majority ele, 2) count majority, 3) find swaps - all in O(N) time
# O(N) space since we combine (for code brevity) but actually can keep to O(1) if just count in-place
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Boyer-Moore to find majority
        curr = -1
        votes = 1
        combined = tops + bottoms
        n = len(tops)
        for num in combined:
            if num == curr:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    curr = num
                    votes = 1
        if combined.count(curr) < n:
            return -1

        swap_top, swap_bottom = 0, 0
        for i in range(n):
            if tops[i] != curr and bottoms[i] != curr:
                return -1
            if bottoms[i] == curr and tops[i] != curr:
                swap_top += 1
            elif tops[i] == curr and bottoms[i] != curr:
                swap_bottom += 1
        return min(swap_top, swap_bottom)
