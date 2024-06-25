class Solution:
    def lengthOfLongestSubstring(self, s):

        # Set of characters who have encountered
        chars = {}

        # Pointer and result variable
        left = res = 0

        for right in range(len(s)):

            # If we have encountered this character before, then we increment the pointer
            # to the last seen location of this character
            if s[right] in chars:
                # Update the left pointer to be one position right of the last occurrence of s[right]
                left = max(left, chars[s[right]] + 1)

            # Add this character to the set
            chars[s[right]] = right

            # The longest substring would be this number of characters in the set
            res = max(res, right - left + 1)

        return res

# s = "abcabcbb"
# print(Solution().lengthOfLongestSubstring(s))
# s = "bbbbb"
# print(Solution().lengthOfLongestSubstring(s))
# s = "pwwkew"
# print(Solution().lengthOfLongestSubstring(s))
# s = "abcabcbb"
# print(Solution().lengthOfLongestSubstring(s))
