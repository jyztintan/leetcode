from collections import defaultdict


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


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = defaultdict(int)
        for c in t:
            target_freq[c] += 1

        n = len(s)
        left = right = 0
        curr_freq = defaultdict(int)

        best = []
        min_len = float('inf')

        fulfilled = 0
        while right < n:
            char = s[right]
            if char in target_freq:
                curr_freq[char] += 1
                if curr_freq[char] == target_freq[char]:
                    fulfilled += 1

            while fulfilled == len(target_freq):
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    best = [left, right]

                left_char = s[left]
                if left_char in target_freq:
                    curr_freq[left_char] -= 1
                    if curr_freq[left_char] < target_freq[left_char]:
                        fulfilled -= 1

                left += 1

            right += 1

        if best:
            return s[best[0]:best[1] + 1]
        return ""

# Check if it correctly returns when there is one possible permutations
s = "ABCD"
t = "ABC"
assert Solution().minWindow(s, t) == "ABC"

# Check if it correctly returns shortest if there are multiple possible permutations
s = "ADOBECODEBANC"
t = "ABC"
assert Solution().minWindow(s, t) == "BANC"

# # Empty String
# s = "ABC"
# t = ""
# assert Solution().minWindow(s, t) == ""

# No valid substring permutation
s = "A"
t = "ABCD"
assert Solution().minWindow(s, t) == ""