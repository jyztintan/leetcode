class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        binaries = set()
        for left in range(len(s) - k + 1):
            window = s[left:left + k]
            binaries.add(window)
        return len(binaries) == 2 ** k
