# Both solutions are O(N) but the first solution (while may take longer in terms of absolute time, seems more elegant
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        return new_str == new_str[::-1]

class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left_ptr, right_ptr = 0, n - 1
        while left_ptr < right_ptr:
            while not s[left_ptr].isalnum():
                left_ptr += 1
                if left_ptr == n:
                    return True
            while not s[right_ptr].isalnum():
                right_ptr -= 1
                if right_ptr == 0:
                    return True
            if s[left_ptr].lower() != s[right_ptr].lower():
                return False
            left_ptr += 1
            right_ptr -= 1
        return True

# s1 = "A man, a plan, a canal: Panama"
# sol = Solution()
# print(sol.isPalindrome(s1))
