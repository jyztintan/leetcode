class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # If there are more letters in s1 than s2, impossible for s2 to have a permutation substring s1
        if len(s1) > len(s2):
            return False

        # Keep track of letters we are accounting for
        original = [0] * 26
        window = [0] * 26
        letter_order = ord('a')

        # Increment the relevant letter buckets of s1
        for c in s1:
            original[ord(c) - letter_order] += 1

        # The first window is the first len(s1) letters in s2
        for i in range(len(s1)):
            window[ord(s2[i]) - letter_order] += 1

        # We incrementally slide the window while there is no matching list
        for i in range(len(s1), len(s2)):
            if window == original:
                return True
            window[ord(s2[i - len(s1)]) - letter_order] -= 1
            window[ord(s2[i]) - letter_order] += 1

        return window == original

# print(Solution().checkInclusion("ab","eidbaooo"))
# print(Solution().checkInclusion("ab","eidboaoo"))
# print(Solution().checkInclusion("mart","karma"))
