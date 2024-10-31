class Solution(object):
    def triangleType(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sides = set(nums)

        n = len(sides)
        large = max(sides)

        # If the triangle property: length of any side < sum(other 2 sides) does not hold
        if large >= sum(nums) - large:
            return "none"
        # All 3 side lengths are the same
        if n == 1:
            return "equilateral"
        # 2 side lengths are the same
        if n == 2:
            return "isosceles"
        # 3 different side lengths
        return "scalene"

