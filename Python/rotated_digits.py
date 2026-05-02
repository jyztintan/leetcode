class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        for num in range(1, n + 1):
            s = str(num)
            invalid = False
            valid = False
            for c in s:
                if c in "347":
                    invalid = True
                    break
                elif c in "2569":
                    valid = True
            if not invalid and valid:
                count += 1
        return count
