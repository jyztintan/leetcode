class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        turned_on = []
        for day, bulb in enumerate(bulbs, 1):
            idx = bisect.bisect(turned_on, bulb)
            if idx > 0:
                left_adj = turned_on[idx - 1]
                if abs(bulb - left_adj) - 1 == k:
                    return day
            if idx < len(turned_on):
                right_adj = turned_on[idx]
                if abs(bulb - right_adj) - 1 == k:
                    return day
            turned_on.insert(idx, bulb)
        return -1
