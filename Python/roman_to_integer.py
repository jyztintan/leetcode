class Solution:
    def romanToInt(self, s: str) -> int:
        n = len(s)
        special = {"IV" : 4, "IX" : 9, "XL": 40, "XC": 90, "CD": 400, "CM" : 900}
        normal = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        ptr = 0
        total = 0
        while ptr < n:
            substr = s[ptr:ptr + 2]
            if substr in special:
                total += special[substr]
                ptr += 2
            else:
                total += normal[s[ptr]]
                ptr += 1
        return total

# print(Solution().romanToInt("MCMXCIV"))

