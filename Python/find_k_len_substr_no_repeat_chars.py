class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        window = {}
        repeated = 0
        if k > len(s):
            return 0
        # Starting window
        for ptr in range(k):
            c = s[ptr]
            window[c] = window.get(c, 0) + 1
            if window[c] == 2:
                repeated += 1

        ans = 0
        if repeated == 0:
            ans += 1

        for left in range(len(s) - k):
            left_c = s[left]
            window[left_c] -= 1
            if window[left_c] == 1:
                repeated -= 1
            right_c = s[left + k]
            window[right_c] = window.get(right_c, 0) + 1
            if window[right_c] == 2:
                repeated += 1
            if repeated == 0:
                ans += 1
        return ans
