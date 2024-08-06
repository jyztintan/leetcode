class Solution:
    def minimumPushes(self, word: str) -> int:
        # The higher the frequency of the character, the lower the num of pushes we want
        freq = {}
        for c in word:
            freq[c] = freq.get(c, 0) + 1

        # Sort the frequencies in non-increasing order and map higher frequencies to 1 push,
        # mid frequencies to 2 pushes and lower frequencies to 3.
        sorted_freq = sorted(list(freq.values()), reverse=True)
        ans = 0
        count = 0
        push = 1
        for num in sorted_freq:
            ans += push * num
            count += 1

            if count == 8:
                count = 0
                push += 1
        return ans

# print(Solution().minimumPushes("abcdea"))
