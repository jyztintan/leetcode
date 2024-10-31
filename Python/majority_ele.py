class Solution:
    def majorityElement(self, nums) -> int:
        # Boyer-Moore goes HARD
        count = 0
        lezgoo = None
        for num in nums:
            if count == 0:
                lezgoo = num
                count = 1
            elif num == lezgoo:
                count += 1
            else:
                count -= 1
        return lezgoo

