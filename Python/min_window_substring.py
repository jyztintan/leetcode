class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        ans = [-1, -1]
        ans_length = float('inf')

        # Keep track of letters we are accounting for
        original = {}
        window = {}
        left = 0

        # Increment the relevant letter buckets of t
        for c in t:
            original[c] = original.get(c, 0) + 1

        # We want to meet all required letters of the substring
        target = 0

        # We iterate the right pointer incrementally
        for right in range(len(s)):
            char = s[right]

            # If the right pointer character is in the substring
            if char in original:

                # Update our window tracker
                window[char] = window.get(char, 0) + 1

                # If it meets the requirement then we can increment one target
                if window[char] == original[char]:
                    target += 1

            # If our new substring window meets the target
            while target == len(original):

                # We take note of this substring if it is less than what we currently have
                if right - left + 1 < ans_length:
                    ans = [left, right]
                    ans_length = right - left + 1

                # If the left pointer is a character in our substring, we need to decrement it accordingly as we move our left pointer up
                if s[left] in original:
                    window[s[left]] -= 1
                    if window[s[left]] < original[s[left]]:
                        target -= 1
                left += 1

        # If after going through our pointers, the answer was not modified, it means we have no valid substring
        if ans_length == float('inf'):
            return ""

        l, r = ans
        return s[l:r+1]

# s = "ADOBECODEBANC"
# t = "ABC"
# print(Solution().minWindow(s, t))