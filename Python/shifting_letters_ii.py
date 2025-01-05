from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shifting = [0] * (n + 1)
        for start, end, direction in shifts:
            if direction:
                shifting[start] += 1
                shifting[end + 1] -= 1
            else:
                shifting[start] -= 1
                shifting[end + 1] += 1

        word = []
        curr_shift = 0
        for idx in range(n):
            curr_shift += shifting[idx]
            unicode = (ord(s[idx]) - ord('a') + curr_shift) % 26 + ord('a')
            c = chr(unicode)
            word.append(c)
        return "".join(word)

shifts = [[0,1,0],[1,2,1],[0,2,1]]
print(Solution().shiftingLetters("abc", shifts))