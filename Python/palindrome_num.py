class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        num = str(x)
        left, right = 0, len(num) - 1
        while left < right:
            if num[left] != num[right]:
                return False
            left += 1
            right -= 1
        return num[left] == num[right]