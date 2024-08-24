class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        if length == 1:
            return str(int(n) - 1)
        possible = []
        possible.append(str(10 ** length + 1))
        possible.append(str(10 ** (length - 1) - 1))

        mid = (length - 1) // 2
        prefix = int(n[:mid + 1])
        for i in range(-1, 2, 1):
            num = first_half = str(prefix + i)
            if length % 2:
               num += first_half[:-1][::-1]
            else:
                num += first_half[::-1]

            possible.append(num)

        best = (float('inf'), "")
        for pos in possible:
            if pos == n:
                continue
            diff = abs(int(pos) - int(n))
            if diff < best[0]:
                best = (diff, pos)
        return best[1]



print(Solution().nearestPalindromic("4"))
print(Solution().nearestPalindromic("10"))
print(Solution().nearestPalindromic("45654"))


