class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        valid = False
        for i in range(len(s)):
            if i == 0:
                if not s[i].isdigit() and s[i] not in '+-':
                    return 0
                if s[i].isdigit():
                    valid = True

            else:
                if not s[i].isdigit():
                    i -= 1
                    break
                else:
                    valid = True

        if not valid:
            return 0
        ans = int(s[:i + 1])
        if ans > 2 ** 31 -  1:
            return 2 ** 31 - 1
        elif ans < -2 ** 31:
            return -2 ** 31
        return ans

print(Solution().myAtoi("-f2"))