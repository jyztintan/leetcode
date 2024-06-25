class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Keeps track of the number of times each character appears within our window
        d = {"":0}

        # most_popular: The frequency of the most common char in our window
        # ans: Length of longest substring containing the same letter after k replacements
        # left: Pointer representing the left side of the window
        most_popular = ans = left = 0

        for right in range(len(s)):

            # Right side of the window
            curr = s[right]

            # If it is a new character, then initialised as 0 + 1. Otherwise, just increment the respective character's count
            d[curr] = d.get(curr, 0) + 1

            # The highest frequency is either the one we saw already or the newly incremented character count
            most_popular = max(most_popular, d[curr])

            # If the current subarray window exceeds the number of allowable replacements, we need to shrink the window
            if right - left + 1 - most_popular > k:
                d[s[left]] -= 1
                left += 1

                # The highest frequency achieved so far cannot be exceeded by any other character just by removing characters. Hence, the lines below are not needed
                # if s[left - 1] == most_popular - 1:
                #     most_popular = max(d.values())

            ans = max(ans, right - left + 1)

        return ans

# s = "ABABB"
# print(Solution().characterReplacement(s, 2))
# s = "AABABBA"
# print(Solution().characterReplacement(s, 1))
# s = "BAAA"
# print(Solution().characterReplacement(s, 0))