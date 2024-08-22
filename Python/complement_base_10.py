class Solution:
    def bitwiseComplement(self, num: int) -> int:
        if not num:
            return 1
        binary = ""
        while num:
            if num % 2:
                binary = "0" + binary
            else:
                binary = "1" + binary
            num //= 2

        ans = 0
        n = len(binary) - 1
        for bit in binary:
            ans += 2 ** (n) * int(bit)
            n -= 1
        return ans

# print(Solution().bitwiseComplement(0))
