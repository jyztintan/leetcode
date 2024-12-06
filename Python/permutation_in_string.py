class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)

        # If there are more letters in s1 than s2, impossible for s2 to have a permutation substring s1
        if n > m:
            return False

        # Keep track of letter frequencies
        target = [0] * 26
        window = [0] * 26

        for c in s1:
            target[ord(c) - ord('a')] += 1

        # Initialise window for s2
        for i in range(n):
            window[ord(s2[i]) - ord('a')] += 1

        # We incrementally slide the window while there is no matching list
        left = 0
        for right in range(n, len(s2)):
            if window == target:
                return True
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1
            window[ord(s2[right]) - ord('a')] += 1

        return window == target

# Simple test case
assert Solution().checkInclusion('abc', 'abcdef')

# No permutation
assert Solution().checkInclusion('abz', 'abcdef') == False

# Permutation in middle
assert Solution().checkInclusion('edc', 'abcdef')

# Empty string as s1
assert Solution().checkInclusion('', 'abcdef')

# s1 == s2
assert Solution().checkInclusion('abc', 'abc')