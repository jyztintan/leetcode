class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def is_alphanumeric(c):
            return c.isalpha() or c.isnumeric()

        start = 0
        end = len(s) - 1
        while True:
            while not is_alphanumeric(s[start]) and start < len(s) - 1:
                start += 1
            while not is_alphanumeric(s[end]) and end > 0:
                end -= 1
            if start >= end:
                break
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True
        
s1 = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s1))